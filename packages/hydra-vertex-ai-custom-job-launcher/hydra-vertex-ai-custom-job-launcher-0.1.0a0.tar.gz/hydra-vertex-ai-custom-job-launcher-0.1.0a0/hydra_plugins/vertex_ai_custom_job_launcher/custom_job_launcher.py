from __future__ import annotations
import logging
from typing import Optional, Sequence
import os

from hydra.types import HydraContext
from hydra.core.singleton import Singleton
from hydra.core.utils import (
    JobReturn,
    configure_log,
    filter_overrides,
    setup_globals,
)
from hydra.plugins.launcher import Launcher
from hydra.types import TaskFunction
from omegaconf import DictConfig, open_dict

log = logging.getLogger(__name__)

def launch_custom_jobs(
    launcher: VertexAICustomJobLauncher,
    job_overrides: Sequence[Sequence[str]],
    initial_job_idx: int,
) -> Sequence[JobReturn]:
    """
    Launch as many custom jobs as there are job overrides.
    """

    # Lazy imports, to avoid slowing down the registration of all other plugins
    import hydra
    import cloudpickle
    import fsspec
    import gcsfs
    from google.cloud import aiplatform

    # Set up the custom job execution requirements
    custom_job_exec_requirements = [
        f"hydra-core=={hydra.__version__}",
        f"cloudpickle=={cloudpickle.__version__}",
        f"fsspec=={fsspec.__version__}",
        f"gcsfs=={gcsfs.__version__}",
    ]

    # Set up global Hydra variables
    setup_globals()

    # Assert that the launcher has been set up
    assert launcher.config is not None
    assert launcher.hydra_context is not None
    assert launcher.task_function is not None

    # Configure the logging subsystem
    configure_log(launcher.config.hydra.hydra_logging, 
                  launcher.config.hydra.verbose)

    # Initialize Vertex AI
    log.info(f"Initializing Vertex AI with:")
    log.info(f"- Project: {launcher.project_id}")
    log.info(f"- Location: {launcher.location}")
    log.info(f"- Staging_bucket: {launcher.staging_bucket}")
    log.info(f"- Experiment: {launcher.experiment}")
    log.info(f"- Experiment_tensorboard: {launcher.experiment_tensorboard}")
    aiplatform.init(
        project=launcher.project_id,
        location=launcher.location,
        staging_bucket=launcher.staging_bucket,
        experiment=launcher.experiment,
        experiment_tensorboard=launcher.experiment_tensorboard
    )

    # For each job override:
    # - Load the sweep config and set the job id and job num.
    # - Pickle the job specs (hydra context, sweep config, task function and singleton state) into a temporary directory.
    # - Initialize the Vertex AI Custom Job, setting the container spec command to the task script and
    #   the container spec args to the temporary directory.
    # - Submit the job asynchronously.
    jobs: list[aiplatform.CustomJob] = []
    temp_dirs: list[str] = []
    log.info(f"Launching {len(job_overrides)} custom jobs on Vertex AI...")
    for idx, overrides in enumerate(job_overrides):

        # Set the job id from the initial job idx and the current idx
        idx = initial_job_idx + idx

        # Log the job id and overrides
        lst = " ".join(filter_overrides(overrides))
        log.info(f"- #{idx} : {lst}")

        # Load the sweep config and set the job num
        log.info(f"Loading sweep config for job #{idx}...")
        sweep_config = launcher.hydra_context.config_loader.load_sweep_config(
            launcher.config, list(overrides)
        )
        with open_dict(sweep_config):
            sweep_config.hydra.job.num = idx

        # Initialize the temporary directory from :
        # - The staging bucket URL of the Vertex AI Custom Job
        # - The hydra sweep directory
        # - The hydra sweep subdir
        temp_dir = os.path.join(
            launcher.staging_bucket,
            sweep_config.hydra.sweep.dir,
            sweep_config.hydra.sweep.subdir
        )
        log.info(f"Initializing temporary directory for job #{idx} at {temp_dir}...")
        temp_dirs.append(temp_dir)
        fsspec.open(temp_dir, "wb+").close()

        # Pickle the job specs, so that they can be passed to the custom job.
        log.info(f"Pickling job specs for job #{idx} to {temp_dir}/job_specs.pkl...")
        job_specs = {
            "hydra_context": launcher.hydra_context,
            "sweep_config": sweep_config,
            "task_function": launcher.task_function,
            "singleton_state": Singleton.get_state(),
        }
        with fsspec.open(f"{temp_dir}/job_specs.pkl", "wb") as f:
            cloudpickle.dump(job_specs, f)

        # Initialize the custom job with the execution script as the command and the temporary directory as the args
        log.info(f"Initializing custom job #{idx}...")
        custom_job_exec_script_path = str(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "_custom_job_exec.py"
        ))
        job = aiplatform.CustomJob.from_local_script(
            display_name=launcher.display_name,
            script_path=custom_job_exec_script_path,
            container_uri=launcher.container_uri,
            args=[str(temp_dir)],
            requirements=custom_job_exec_requirements,
            machine_type=launcher.machine_type,
            accelerator_type=launcher.accelerator_type,
            accelerator_count=launcher.accelerator_count,
            boot_disk_type=launcher.boot_disk_type,
            boot_disk_size_gb=launcher.boot_disk_size_gb,
            base_output_dir=launcher.base_output_dir
        )

        # Submit the job
        log.info(f"Submitting custom job #{idx}...")
        job.submit(service_account=launcher.service_account_email)
        
        # Append the job to the list of jobs
        jobs.append(job)

    # Wait for the jobs to complete
    log.info("Waiting for the jobs to complete...")
    for job in jobs:
        log.info(f"Waiting for job {job.name} to complete...")
        while job.state not in [aiplatform.gapic.JobState.JOB_STATE_SUCCEEDED,
                                aiplatform.gapic.JobState.JOB_STATE_FAILED,
                                aiplatform.gapic.JobState.JOB_STATE_CANCELLED]:
            pass
        log.info(f"Job {job.name} completed with state {job.state}.")

    # Read the job returns and delete the temporary directories
    log.info("Reading the job returns...")
    job_returns: list[JobReturn] = []
    for temp_dir in temp_dirs:
        log.info(f"Reading the job return from {temp_dir}/job_returns.pkl...")
        with fsspec.open(f"{temp_dir}/job_returns.pkl", "rb") as f:
            job_return = cloudpickle.load(f)
        log.info(f"Job return: {job_return}")
        job_returns.append(job_return)
        log.info(f"Deleting temporary directory {temp_dir}...")
        fs_url: tuple[fsspec.AbstractFileSystem, ...] = fsspec.core.url_to_fs(temp_dir)
        fs = fs_url[0]
        fs.rm(temp_dir, recursive=True)

    # Return the job returns
    return job_returns

class VertexAICustomJobLauncher(Launcher):

    def __init__(
        self,
        **kwargs
    ) -> None:
        
        self.config: Optional[DictConfig] = None
        self.task_function: Optional[TaskFunction] = None
        self.hydra_context: Optional[HydraContext] = None

        for key, value in kwargs.items():
            setattr(self, key, value)

    def setup(
        self,
        *,
        hydra_context: HydraContext,
        task_function: TaskFunction,
        config: DictConfig,
    ) -> None:
        self.config = config
        self.hydra_context = hydra_context
        self.task_function = task_function

    def launch(
        self, job_overrides: Sequence[Sequence[str]], initial_job_idx: int
    ) -> Sequence[JobReturn]:
        """
        :param job_overrides: a List of List<String>, where each inner list is the arguments for one job run.
        :param initial_job_idx: Initial job idx in batch.
        :return: an array of return values from run_job with indexes corresponding to the input list indexes.
        """
        return launch_custom_jobs(self, job_overrides, initial_job_idx)

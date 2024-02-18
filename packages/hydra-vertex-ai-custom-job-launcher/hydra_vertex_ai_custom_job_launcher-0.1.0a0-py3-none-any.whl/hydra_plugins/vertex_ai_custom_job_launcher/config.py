# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from dataclasses import dataclass

from hydra.core.config_store import ConfigStore

@dataclass
class VertexAICustomJobLauncherConf:
    project_id: str
    location: str
    staging_bucket: str
    experiment: str
    experiment_tensorboard: bool | str
    display_name: str
    container_uri: str
    machine_type: str
    accelerator_type: str
    accelerator_count: int
    boot_disk_type: str
    boot_disk_size_gb: int
    base_output_dir: str
    service_account_email: str
    _target_: str = (
        "hydra_plugins.vertex_ai_custom_job_launcher.custom_job_launcher.VertexAICustomJobLauncher"
    )

ConfigStore.instance().store(
    group="hydra/launcher",
    name="vertex_ai_custom_job",
    node=VertexAICustomJobLauncherConf,
    provider="vertex_ai_custom_job_launcher",
)
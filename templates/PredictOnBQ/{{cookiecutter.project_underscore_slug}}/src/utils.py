# -*- coding: utf-8 -*-

"""Utility methods."""

import os
import uuid

from apache_beam.options.pipeline_options import PipelineOptions, SetupOptions


def configure_pipeline(
    project,
    artifact_bucket,
    num_workers,
    region,
    machine_type,
    disk_size,
    local=True,
):
    """Configure pipeline options.

    Parameters
    ----------
    project : str
        Project name to run the pipeline
    artifact_bucket : str
        Google Cloud Storage (GCS) bucket to store temp and staging files
    num_workers : int
        Number of workers to run
    region : str
        Region where the project is located
    machine_type : str
        Machine type for running the commands
    disk_size : int
        Disk size for each worker
    local : bool
        If true, runs on test environment else, on Dataflow

    Returns
    -------
    apache_beam.options.pipeline_options.PipelineOptions
        Configuration for the pipeline
    """
    runner = "DataflowRunner" if not local else "DirectRunner"

    pipeline_options = PipelineOptions(
        [
            f"--project={project}",
            f"--runner={runner}",
            f"--temp_location={os.path.join(artifact_bucket, 'temp')}",
            f"--staging_location={os.path.join(artifact_bucket, 'staging')}",
            f"--job_name={{cookiecutter.project_slug}}-{uuid.uuid4().hex}",
            f"--num_workers={num_workers}",
            f"--region={region}",
            f"--autoscaling_algorithm=NONE",
            "--requirements_file=requirements-worker.txt",
            f"--worker_machine_type={machine_type}",
            "--setup_file=./setup.py",
            f"--disk_size_gb={disk_size}",
        ]
    )

    pipeline_options.view_as(SetupOptions).save_main_session = True
    return pipeline_options

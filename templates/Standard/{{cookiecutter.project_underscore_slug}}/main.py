# -*- coding: utf-8 -*-

"""Entrypoint for Dataflow Pipeline."""

import apache_beam as beam
import click

from src.utils import configure_pipeline


@click.option(
    "-n",
    "--num-workers",
    default=8,
    help="Number of workers to run the Dataflow job",
)
@click.option(
    "-m",
    "--machine-type",
    default="n1-standard-4",
    help="Machine type to run the jobs on",
)
@click.option(
    "-s",
    "--disk-size",
    default=10,
    help="Disk size (in GB) for each worker when job is run",
)
@click.option(
    "--project",
    type=str,
    default="{{cookiecutter.gcp_project}}",
    help="Google Cloud Platform (GCP) project to run the Dataflow job",
)
@click.option(
    "--region",
    type=str,
    default="{{cookiecutter.gcp_region}}",
    help="Google Cloud Platform (GCP) region to run the Dataflow job",
)
@click.option(
    "--artifact-bucket",
    type=str,
    default="{{cookiecutter.gcs_artifact_bucket}}",
    help="Cloud Storage bucket to store temp and staging files",
)
@click.option("--local", is_flag=True, help="Run on local machine")
def run(**opts):
    """Run the Dataflow pipeline."""
    pipeline_options = configure_pipeline(
        project=opts["project"],
        artifact_bucket=opts["artifact_bucket"],
        num_workers=opts["num_workers"],
        region=opts["region"],
        machine_type=opts["machine_type"],
        disk_size=opts["disk_size"],
        local=opts["local"],
    )

    with beam.Pipeline(options=pipeline_options) as p:
        # Your Dataflow Pipeline goes here
        # Learn more about writing Dataflow pipelines in this link:
        # https://cloud.google.com/dataflow/docs/quickstarts
        pass


if __name__ == "__main__":
    run()

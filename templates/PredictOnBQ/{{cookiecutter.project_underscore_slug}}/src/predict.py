# -*- coding: utf-8 -*-

"""ML related functions for prediction"""

import logging
from subprocess import check_output, CalledProcessError, STDOUT


def predict_fn(rows):
    """Predict function.

    This is the workhorse predict function that takes in a BigQuery row and
    runs the inference model on it.



    """


def get_model_from_gcs(
    source_path="{{cookiecutter.model_gcs_path}}", target_path="/tmp/"
):
    """Download a model from Google Cloud Storage.

    Parameters
    ----------
    source_path : string
        Google Cloud Storage URI of the model file
    target_path : string
        Local directory to store the model into
    """
    run_command("gsutil -m cp -r {source_path} {target_path}")


def run_command(cmd, raise_on_error=True):
    """Run a command in the command line.

    Parameters
    ----------
    cmd : string
        The command to be run
    raise_on_error : bool
        Raise an exception when an error is encountered

    """
    try:
        logging.info(cmd)
        return check_output(cmd, shell=True, stderr=STDOUT)
    except CalledProcessError as e:
        logging.error(f"Error on {cmd}: {e.output}")
        if raise_on_error:
            raise ValueError(e.output)

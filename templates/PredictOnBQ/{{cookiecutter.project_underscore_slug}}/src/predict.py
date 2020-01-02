# -*- coding: utf-8 -*-

"""ML related functions for prediction"""

import os
import logging
from subprocess import check_output, CalledProcessError, STDOUT

import joblib


def predict_fn(rows, model_source_path):
    """Predict function.

    This is the workhorse predict function that takes in a BigQuery row and
    runs the inference model on it. Write the predict function in such a way
    that your model can easily be loaded.

    For now, it's assumed that the model can be loaded via the `joblib`
    library. This is specific for a whole range of scikit-learn or scikit-based
    implementations. Feel free to change it to your preferred loading scheme.

    Parameters
    ----------
    rows : 2-tuple
        The rows here are grouped by its primary key. The first element
        corresponds to the primary key while the second element is a list of
        dicts. For example:

        (pKey1, [{col1a: val1a, col2a: val2a}, {col1b: val1b, col2b, val2b}])

    model_source_path : string
        The full GCS link for the model source
    """
    samples = rows[1]
    model_local_path = get_model_from_gcs(model_source_path)

    # TODO (Optional): Update the model loading scheme.
    # This cookiecutter assumes that you're writing scikit-learn models and
    # saving them as joblib artifacts.
    model = joblib.load(model_local_path)

    # TODO (Optional): Update predict method based on model.
    # Here, you can do the following:
    #   * Add preprocessing on values obtained from the sample.
    #   * Update the output dictionary based on your model and the predictions.
    predictions = []
    logging.info("Running predictions")
    for sample in samples:
        preds = model.predict(sample.values())
        predictions.append({"prediction": argmax(preds)})
    return predictions


def argmax(l):
    f = lambda i: l[i]
    return max(range(len(l)), key=f)


def get_model_from_gcs(model_source_path, target_path="/tmp/"):
    """Download a model from Google Cloud Storage.

    Parameters
    ----------
    source_path : string
        Google Cloud Storage URI of the model file
    target_path : string
        Local directory to store the model into

    Returns
    -------
    string
        Model path in the worker machine
    """
    run_command("gsutil -m cp -r {model_source_path} {target_path}")
    return os.path.join(target_path, os.path.basename(model_source_path))


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

# -*- coding: utf-8 -*-

"""Sub-command for creating a new Dataflow project."""

import json
import sys

import click
from cookiecutter.exceptions import (
    FailedHookException,
    InvalidModeException,
    InvalidZipRepository,
    OutputDirExistsException,
    RepositoryCloneFailed,
    RepositoryNotFound,
    UndefinedVariableInTemplate,
    UnknownExtension,
)
from loguru import logger
from cookiecutter.main import cookiecutter

from .mixins import configure_logger


@click.command()
@click.option(
    "-t",
    "--template",
    type=click.Choice(["basic"], case_sensitive=False),
    help="Dataflow template to create",
    default="basic",
)
@click.option(
    "-o",
    "--output-dir",
    default=".",
    type=click.Path(),
    help="Where to output the generated project dir into",
)
@click.option(
    "-f",
    "--overwrite-if-exists",
    is_flag=True,
    help="Overwrite the contents of the output directory if it already exists",
)
@click.option(
    "--replay",
    is_flag=True,
    help="Do not prompt for params and use information entered previously",
)
@click.option(
    "--repository",
    type=str,
    help="Git repository to base the templates from",
    default="https://github.com/ljvmiranda921/dataflow-cookiecutter",
)
@click.option(
    "-c",
    "--checkout",
    help="Branch, tag or commit to checkout after git clone",
)
@click.option(
    "--config-file",
    type=click.Path(),
    default=None,
    help="User configuration file",
)
@click.option(
    "--default-config",
    is_flag=True,
    help="Do not load a config file. Use the defaults instead",
)
@click.pass_context
def new(
    ctx,
    template,
    output_dir,
    overwrite_if_exists,
    replay,
    repository,
    checkout,
    config_file,
    default_config,
):
    """Create a new Dataflow project."""
    configure_logger(
        stream_level="DEBUG" if ctx.obj["VERBOSE"] else "INFO",
        debug_file=ctx.obj["DEBUG_FILE"],
    )

    try:
        cookiecutter(
            template=repository,
            # directory=template,   # Add this after 1.7.1 has been released
            checkout=checkout,
            no_input=False,
            extra_context=None,
            replay=replay,
            overwrite_if_exists=overwrite_if_exists,
            output_dir=output_dir,
            config_file=config_file,
            default_config=default_config,
            password=None,
        )
    except (
        OutputDirExistsException,
        InvalidModeException,
        FailedHookException,
        UnknownExtension,
        InvalidZipRepository,
        RepositoryNotFound,
        RepositoryCloneFailed,
    ) as e:
        logger.error(e)
        sys.exit(1)
    except UndefinedVariableInTemplate as undefined_err:
        logger.error("{}".format(undefined_err))
        logger.error("Error message: {}".format(undefined_err.error.message))

        context_str = json.dumps(
            undefined_err.context, indent=4, sort_keys=True
        )
        logger.error("Context: {}".format(context_str))
        sys.exit(1)

    msg = f"""
    Template ({template}) built! Be sure to check the generated
    requirements-worker.txt and README file.
    """

    logger.success(msg)

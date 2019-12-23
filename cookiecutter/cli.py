# -*- coding: utf-8 -*-

"""Dataflow-cookiecutter command-line interface (CLI)"""

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
from cookiecutter.log import configure_logger
from cookiecutter.main import cookiecutter


@click.group()
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Print debug information",
    default=False,
)
@click.option(
    "--debug-file",
    type=click.Path(),
    default=None,
    help="File to be used as a stream for DEBUG logging",
)
@click.pass_context
def main(ctx, verbose, debug_file):
    """dataflow-cookiecutter is a tool for setting-up Dataflow projects"""
    ctx.ensure_object(dict)
    ctx.obj = {"VERBOSE": verbose, "DEBUG_FILE": debug_file}


@main.command()
@click.option("--template", type=click.Choice(["basic"], case_sensitive=False))
@click.option(
    "-f",
    "--overwrite-if-exists",
    is_flag=True,
    help="Overwrite the contents of the output directory if it already exists",
)
@click.option(
    "-o",
    "--output-dir",
    default=".",
    type=click.Path(),
    help="Where to output the generated project dir into",
)
@click.option(
    "--replay",
    is_flag=True,
    help="Do not prompt for parameters and only use information entered previously",
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
    config_file,
    default_config,
):
    """Create a new Dataflow project"""
    configure_logger(
        stream_level="DEBUG" if ctx.obj["VERBOSE"] else "INFO",
        debug_file=ctx.obj["DEBUG_FILE"],
    )

    try:
        cookiecutter(
            template=template,
            checkout=None,
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
        click.echo(e)
        sys.exit(1)
    except UndefinedVariableInTemplate as undefined_err:
        click.echo("{}".format(undefined_err))
        click.echo("Error message: {}".format(undefined_err.error.message))

        context_str = json.dumps(
            undefined_err.context, indent=4, sort_keys=True
        )
        click.echo("Context: {}".format(context_str))
        sys.exit(1)


if __name__ == "__main__":
    main(obj={})

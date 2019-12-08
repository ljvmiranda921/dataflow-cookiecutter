# -*- coding: utf-8 -*-

"""Dataflow-cookiecutter command-line interface (CLI)"""

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
    u"--debug-file",
    type=click.Path(),
    default=None,
    help=u"File to be used as a stream for DEBUG logging",
)
@click.pass_context
def main(ctx, verbose, debug_file):
    """dataflow-cookiecutter is a tool for setting-up Dataflow projects"""
    ctx.ensure_object(dict)
    ctx.obj = {"VERBOSE": verbose, "DEBUG_FILE": debug_file}


@main.command()
@click.pass_context
def new(ctx):
    """Create a new Dataflow project"""
    configure_logger(
        stream_level="DEBUG" if ctx.obj["VERBOSE"] else "INFO",
        debug_file=ctx.obj["DEBUG_FILE"],
    )


if __name__ == "__main__":
    main(obj={})

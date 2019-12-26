# -*- coding: utf-8 -*-

"""Dataflow-cookiecutter command-line interface (CLI)"""

import click

from new import new


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


main.add_command(new)


if __name__ == "__main__":
    main(obj={})
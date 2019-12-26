# -*- coding: utf-8 -*-

"""Sub-command for listing all available templates."""

import os
import json

import click
from tabulate import tabulate
from loguru import logger

from .mixins import configure_logger
from .config import TEMPLATE_CONFIG


@click.command()
@click.pass_context
def ls(ctx):
    """List all available templates."""
    configure_logger(
        stream_level="DEBUG" if ctx.obj["VERBOSE"] else "INFO",
        debug_file=ctx.obj["DEBUG_FILE"],
    )

    logger.debug(f"Loading configuration")
    data = [[k] + v for k, v in TEMPLATE_CONFIG.items()]
    headers = ["Name", "Dir", "Description"]
    print(tabulate(data, headers=headers))

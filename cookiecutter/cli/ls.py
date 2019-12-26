# -*- coding: utf-8 -*-

"""Sub-command for listing all available templates."""

import os
import json

import click
from tabulate import tabulate
from loguru import logger

from mixins import configure_logger


ROOT = os.path.abspath(os.path.dirname(__file__))
INDEX_FILE = os.path.join(ROOT, "index.json")


@click.command()
@click.pass_context
def ls(ctx):
    """List all available templates."""
    configure_logger(
        stream_level="DEBUG" if ctx.obj["VERBOSE"] else "INFO",
        debug_file=ctx.obj["DEBUG_FILE"],
    )

    logger.debug(f"Loading index file: {INDEX_FILE}")
    with open(INDEX_FILE) as f:
        data = json.load(f)

    data_ = [[k] + v for k, v in data.items()]
    headers = ["Name", "Dir", "Description"]
    print(tabulate(data_, headers=headers))

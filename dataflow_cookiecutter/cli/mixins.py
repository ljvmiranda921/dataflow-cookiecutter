# -*- coding: utf-8 -*-

"""Mixins code for the cli module."""

import sys

from loguru import logger


def configure_logger(stream_level, debug_file):
    """Configure logger based on Loguru."""
    logger.remove()
    logger.add(sys.stderr, level=stream_level)
    logger.add(debug_file, level="DEBUG")

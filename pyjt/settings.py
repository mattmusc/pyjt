"""
PYJT
"""
import logging
import os
import platform

__version__ = "0.0.1"
__progname__ = "pyjt"

CWD_DIR = os.path.curdir
MODULE_DIR = os.path.dirname(__file__)
OS = platform.uname()[0]
LOGGING_LEVEL = logging.INFO
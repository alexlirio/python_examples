import logging.config
import json
import os

"""
Logger Module

This module is responsible for create logging objects in order to process
LOG operations.

Attributes:
    parent_dir: parent directory in whih CONFIG file can be founded.
    log_file: file which contains logging configuration
"""
parent_dir = os.path.dirname(__file__)
config_file = os.path.join(parent_dir, 'config.json')
if os.path.exists(config_file):
    with open(config_file, 'rt') as f:
        config = json.load(f)
    logging.config.dictConfig(config)
else:
    logging.basicConfig(level=logging.INFO)


def get_logger(module_name):
    """
    Method used to initialize logger object.

    Args:
        module_name (str): Name of the module that involkes logger.
    """
    return logging.getLogger(module_name)

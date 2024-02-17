import os
import logging
from lambdatest_sdk_utils.constants import get_pkg_name

def log_level():
    if os.getenv('LT_SDK_DEBUG') == 'true':
        return logging.DEBUG 
    else:
        log_level_str = os.getenv('LT_SDK_LOG_LEVEL', 'info').lower()
        if log_level_str == 'debug':
            return logging.DEBUG
        elif log_level_str == 'warning':
            return logging.WARNING
        elif log_level_str == 'error':
            return logging.ERROR
        elif log_level_str == 'critical':
            return logging.CRITICAL
        else:
            return logging.INFO 
        

def setup_logger():
    logging.basicConfig(level=log_level())

def get_logger():
    logger = logging.getLogger(get_pkg_name())
    return logger

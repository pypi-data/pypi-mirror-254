import os
import logging
import threading
from mindspore.ops.primitive import constexpr

logging_level = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]


MSA_GLOBAL_LOGGER=None
# The lock for setting up the logger
_setup_logger_lock = threading.Lock()


def _setup_logger():
    level = logging.ERROR
    _MSA_LOG_ENV = os.environ.get('MSA_LOG')
    if _MSA_LOG_ENV:
        try:
            msa_log_level = int(_MSA_LOG_ENV)
            level = logging_level[msa_log_level]
        except:
            raise ValueError(
                f"Incorrect log level, please check the configuration of 'MSA_LOG', desire integer log level: "
                f"4-CRITICAL, 3-ERROR, 2-WARNING, 1-INFO, 0-DEBUG. but got {_MSA_LOG_ENV}."
            ) from None

    global MSA_GLOBAL_LOGGER
    if MSA_GLOBAL_LOGGER:
        _setup_logger_lock.acquire()
        MSA_GLOBAL_LOGGER.setLevel(level)
        _setup_logger_lock.release()

        return MSA_GLOBAL_LOGGER

    logger = logging.getLogger("MindTorch")
    handler = logging.StreamHandler()
    logger.setLevel(level)

    formatter = logging.Formatter("%(asctime)s [%(name)s %(levelname)s]: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    _setup_logger_lock.acquire()
    MSA_GLOBAL_LOGGER = logger
    _setup_logger_lock.release()

    return MSA_GLOBAL_LOGGER


def _get_logger():
    """
    Get logger instance.

    Returns:
        Logger, a logger.
    """
    global MSA_GLOBAL_LOGGER
    if MSA_GLOBAL_LOGGER:
        return MSA_GLOBAL_LOGGER
    logger = _setup_logger()
    return logger

@constexpr
def debug(msg, *args, **kwargs):
    _get_logger().debug(msg, *args, **kwargs)


@constexpr
def info(msg, *args, **kwargs):
    _get_logger().info(msg, *args, **kwargs)


@constexpr
def warning(msg, *args, **kwargs):
    _get_logger().warning(msg, *args, **kwargs)


@constexpr
def error(msg, *args, **kwargs):
    _get_logger().error(msg, *args, **kwargs)


@constexpr
def critical(msg, *args, **kwargs):
    _get_logger().critical(msg, *args, **kwargs)

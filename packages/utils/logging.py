import logging
import structlog


def get_logger(name: str) -> logging.Logger:
    logger = structlog.get_logger(name)
    return logger

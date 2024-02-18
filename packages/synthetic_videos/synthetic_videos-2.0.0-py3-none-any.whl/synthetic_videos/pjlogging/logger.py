"""Main logging component"""
import os
import sys

from loguru import logger

# import watchtower

os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
os.environ["AWS_ACCESS_KEY_ID"] = "AKIAZ5YJNAZVMGIT3LP6"
os.environ["AWS_SECRET_ACCESS_KEY"] = "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"


def init_pjlogger() -> bool:
    """Initializes a file logger."""

    # Detach existing loggers including stderr
    logger.remove()

    log_level = "INFO"
    logger.add(
        "synthetic_videos.log",
        rotation="1 week",
        retention="5 weeks",
        compression="zip",
        level=log_level,
        serialize=True,
    )

    # Configure default stderr logger so that messages can be filtered based on log level.
    logger.add(
        sys.stderr,
        level=log_level,
    )

    return True

"""This module defines the timing decorator.

    Use:

        from decorators.timing import timing

        @timing
        def my_method():
            [do something]

    For a decorated method, two statements will be written to the lob at INFO level:

        (1) A timestamp when the method is started.
        (2) A timestamp when the method ends along with duration in seconds.

    Example log entries:

    2024-02-01T20:31:01::INFO::timing.wrapper()::line-13::
        Function main started at 2024-02-01 20:31:01.455775.
    2024-02-01T20:31:01::INFO::timing.wrapper()::line-21::
        Function main ended at 2024-02-01 20:31:01.456583 with duration 0.001 seconds
"""

import logging
import time
from datetime import datetime

logger = logging.getLogger(__name__)


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        logger.info(f"Function {func.__name__} started at {start_time}.")

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        end_time = datetime.now()
        duration = end - start

        logger.info(
            f"Function {func.__name__} ended at {end_time} "
            f"with duration {duration:.3f} seconds"
        )

        return result

    return wrapper

# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Methods specific to logging utilities."""

import contextlib
import logging
import sys
from datetime import datetime
from typing import Optional, Dict, Any, Iterator, Union
from azureml.metrics.common.exceptions import MetricsException


@contextlib.contextmanager
def default_log_activity(
        logger: logging.Logger,
        activity_name: str,
        activity_type: Optional[str] = None,
        custom_dimensions: Optional[Dict[str, Any]] = None,
) -> Iterator[Optional[Any]]:
    """
    Log the activity status with duration.

    :param logger: logger
    :param activity_name: activity name
    :param activity_type: activity type
    :param custom_dimensions: custom dimensions
    """
    start_time = datetime.utcnow()
    activity_info = {"activity_name": activity_name, "activity_type": activity_type}  # type: Dict[str, Any]
    log_record = {"activity": activity_name, "type": activity_type, "dimesions": custom_dimensions}
    logger.info("[azureml-metrics] ActivityStarted: {}, ActivityType: {},"
                " CustomDimensions: {}".format(activity_name, activity_type, custom_dimensions))
    completion_status = "SUCCESS"
    try:
        yield
    except Exception as e:
        completion_status = "FAILED"
        logger.error(str(e))
        raise
    finally:
        end_time = datetime.utcnow()
        duration_ms = round((end_time - start_time).total_seconds() * 1000, 2)
        activity_info["durationMs"] = duration_ms
        activity_info["completionStatus"] = completion_status

        logger.info(
            "[azureml-metrics] ActivityCompleted: Activity={}, HowEnded={}, Duration={}[ms]".format(
                activity_name, completion_status, duration_ms
            ),
            extra={"properties": activity_info},
        )

    return log_record


def default_log_traceback(
        exception: Union[MetricsException, Exception],
        logger: Optional[Union[logging.Logger, logging.LoggerAdapter]],
        override_error_msg: Optional[str] = None,
        is_critical: Optional[bool] = False,
        tb: Optional[Any] = None,
) -> None:
    """
    Log exception traces.

    :param exception: The exception to log.
    :param logger: The logger to use.
    :param override_error_msg: The message to display that will override the current error_msg.
    :param is_critical: If is_critical, the logger will use log.critical, otherwise log.error.
    :param tb: The traceback to use for logging; if not provided, the one attached to the exception is used.
    """
    if override_error_msg is not None:
        error_msg = override_error_msg
    else:
        error_msg = str(exception)

    # Some exceptions may not have a __traceback__ attr
    traceback_obj = tb or exception.__traceback__ if hasattr(exception, "__traceback__") else None or sys.exc_info()[2]

    exception_class_name = exception.__class__.__name__

    # User can see original log message in their log file
    message = [
        "Class: {}".format(exception_class_name),
        "Message: {}".format(error_msg),
    ]

    if is_critical:
        logger.critical("\n".join(message))
    else:
        logger.error("\n".join(message))

    if traceback_obj is not None and hasattr(traceback_obj, "format_exc"):
        logger.debug(traceback_obj.format_exc())

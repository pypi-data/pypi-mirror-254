# RobotGPT Python bindings.
# 张圣涛 blaze.zhang
import logging
import os
import re
import sys
from enum import Enum
from typing import Optional
from robotgpt.robotgpt_object import RobotGPTObject
from robotgpt.robotgpt_response import RobotGPTResponse
import robotgpt

ROBOTGPT_LOG = os.environ.get("ROBOTGPT_LOG")

logger = logging.getLogger("robotgpt")

__all__ = [
    "log_info",
    "log_debug",
    "log_warn",
    "logfmt",
]

api_token_to_header = (
    lambda token: {"Authorization": f"{token}"}
)



def _console_log_level():
    if robotgpt.log in ["debug", "info"]:
        return robotgpt.log
    elif ROBOTGPT_LOG in ["debug", "info"]:
        return ROBOTGPT_LOG
    else:
        return None


def log_debug(message, **params):
    msg = logfmt(dict(message=message, **params))
    if _console_log_level() == "debug":
        print(msg, file=sys.stderr)
    logger.debug(msg)


def log_info(message, **params):
    msg = logfmt(dict(message=message, **params))
    if _console_log_level() in ["debug", "info"]:
        print(msg, file=sys.stderr)
    logger.info(msg)


def log_warn(message, **params):
    msg = logfmt(dict(message=message, **params))
    print(msg, file=sys.stderr)
    logger.warn(msg)


def logfmt(props):
    def fmt(key, val):
        # Handle case where val is a bytes or bytesarray
        if hasattr(val, "decode"):
            val = val.decode("utf-8")
        # Check if val is already a string to avoid re-encoding into ascii.
        if not isinstance(val, str):
            val = str(val)
        if re.search(r"\s", val):
            val = repr(val)
        # key should already be a string
        if re.search(r"\s", key):
            key = repr(key)
        return "{key}={val}".format(key=key, val=val)

    return " ".join([fmt(key, val) for key, val in sorted(props.items())])


def get_object_classes():
    # This is here to avoid a circular dependency
    from openai.object_classes import OBJECT_CLASSES

    return OBJECT_CLASSES


def convert_to_openai_object(
    resp,
    api_token=None,
    plain_old_data=False,
):
    # If we get a OpenAIResponse, we'll want to return a OpenAIObject.

    response_ms: Optional[int] = None
    if isinstance(resp, RobotGPTResponse):
        response_ms = resp.response_ms
        resp = resp.data

    if plain_old_data:
        return resp
    elif isinstance(resp, list):
        return [
            convert_to_openai_object(
                i, api_token
            )
            for i in resp
        ]
    elif isinstance(resp, dict) and not isinstance(
        resp, RobotGPTObject
    ):
        resp = resp.copy()
        klass_name = resp.get("object")
        if isinstance(klass_name, str):
            klass = get_object_classes().get(
                klass_name, RobotGPTObject
            )
        else:
            klass = RobotGPTObject

        return klass.construct_from(
            resp,
            api_token=api_token,
            response_ms=response_ms,
        )
    else:
        return resp


def convert_to_dict(obj):
    """Converts a OpenAIObject back to a regular dict.

    Nested OpenAIObjects are also converted back to regular dicts.

    :param obj: The OpenAIObject to convert.

    :returns: The OpenAIObject as a dict.
    """
    if isinstance(obj, list):
        return [convert_to_dict(i) for i in obj]
    # This works by virtue of the fact that OpenAIObjects _are_ dicts. The dict
    # comprehension returns a regular dict and recursively applies the
    # conversion to each value.
    elif isinstance(obj, dict):
        return {k: convert_to_dict(v) for k, v in obj.items()}
    else:
        return obj


def merge_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def default_api_token() -> str:
    if robotgpt.api_token is not None:
        return robotgpt.api_token
    else:
        raise robotgpt.error.AuthenticationError(
            "No API token provided. You can set your API token in code using 'robotgpt.api_token = <API-TOKEN>', or you can set the environment variable ROBOTGPT_API_TOKEN=<API-TOKEN>).You can generate API TOKEN in the ROBOTGPT web interface. See https://dataai-doc.dataarobotics.com/docs/getting-started/authentication for details."
        )

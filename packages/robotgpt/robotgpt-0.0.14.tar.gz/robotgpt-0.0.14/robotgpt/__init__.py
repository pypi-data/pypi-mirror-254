# RobotGPT Python bindings.
# 张圣涛 blaze.zhang
import os
from contextvars import ContextVar
from typing import Optional, TYPE_CHECKING
from robotgpt.chat_completion import ChatCompletion
from robotgpt.error import APIError, InvalidRequestError, RobotGPTError

if TYPE_CHECKING:
    from aiohttp import ClientSession

api_token = os.environ.get("ROBOTGPT_API_TOKEN")
api_url = os.environ.get("ROBOTGPT_API_URL", "https://dataai.harix.iamidata.com/llm/api/ask")
verify_ssl_certs = True  # No effect. Certificates are always verified.
app_info = None
enable_telemetry = False  # Ignored; the telemetry feature was removed.
ca_bundle_path = None  # No longer used, feature was removed
debug = False
log = None  # Set to either 'debug' or 'info', controls console logging

aiosession: ContextVar[Optional["ClientSession"]] = ContextVar(
    "aiohttp-session", default=None
)  # Acts as a global aiohttp ClientSession that reuses connections.
# This is user-supplied; otherwise, a session is remade for each request.

__all__ = [
    "APIError",
    # "Audio",
    "ChatCompletion",
    # "Completion",
    # "Customer",
    # "Edit",
    # "Image",
    # "Deployment",
    # "Embedding",
    # "Engine",
    # "ErrorObject",
    # "File",
    # "FineTune",
    "InvalidRequestError",
    # "Model",
    # "Moderation",
    "RobotGPTError",
    "api_url",
    "api_token",
    "app_info",
    "ca_bundle_path",
    "debug",
    "enable_telemetry",
    "log",
    "verify_ssl_certs",
]

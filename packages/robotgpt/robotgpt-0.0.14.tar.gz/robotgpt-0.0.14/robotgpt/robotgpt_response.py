# RobotGPT Python bindings.
# 张圣涛 blaze.zhang
from typing import Optional


class RobotGPTResponse:
    def __init__(self, data, headers):
        self._headers = headers
        self.data = data

    @property
    def request_id(self) -> Optional[str]:
        return self._headers.get("request-id")

    @property
    def response_ms(self) -> Optional[int]:
        h = self._headers.get("RobotGPT-Processing-Ms")
        return None if h is None else round(float(h))

# RobotGPT Python bindings.
# 张圣涛 blaze.zhang
from urllib.parse import quote_plus

import robotgpt
from robotgpt import error, util
from robotgpt.robotgpt_object import RobotGPTObject
from typing import Optional

from robotgpt import api_requestor


class APIResource(RobotGPTObject):

    @classmethod
    def retrieve(
        cls, id, api_token=None, request_id=None, request_timeout=None, **params
    ):
        instance = cls(id=id, api_token=api_token, **params)
        instance.refresh(request_id=request_id, request_timeout=request_timeout)
        return instance

    @classmethod
    def aretrieve(
        cls, id, api_token=None, request_id=None, request_timeout=None, **params
    ):
        instance = cls(id=id, api_token=api_token, **params)
        return instance.arefresh(request_id=request_id, request_timeout=request_timeout)

    def refresh(self, request_id=None, request_timeout=None):
        self.refresh_from(
            self.request(
                "get",
                self.instance_url(),
                request_id=request_id,
                request_timeout=request_timeout,
            )
        )
        return self

    async def arefresh(self, request_id=None, request_timeout=None):
        self.refresh_from(
            await self.arequest(
                "get",
                self.instance_url(operation="refresh"),
                request_id=request_id,
                request_timeout=request_timeout,
            )
        )
        return self

    # The `method_` and `url_` arguments are suffixed with an underscore to
    # avoid conflicting with actual request parameters in `params`.
    @classmethod
    def _static_request(
        cls,
        method_,
        api_token=None,
        api_url=None,
        request_id=None,
        model=None,
        **params,
    ):
        requestor = api_requestor.APIRequestor(
            api_token,
            api_base=api_url,
            model=model,
        )
        response, _, api_token = requestor.request(
            method_, params, request_id=request_id
        )
        return util.convert_to_openai_object(
            response, api_token
        )

    @classmethod
    async def _astatic_request(
        cls,
        method_,
        api_token=None,
        api_url=None,
        request_id=None,
        model=None,
        **params,
    ):
        requestor = api_requestor.APIRequestor(
            api_token,
            api_url=api_url,
            model=model,
        )
        response, _, api_token = await requestor.arequest(
            method_, params, request_id=request_id
        )
        return response


# RobotGPT Python bindings.
# 张圣涛 blaze.zhang
import time
from pydoc import apropos
from typing import Optional
from urllib.parse import quote_plus

import robotgpt
from robotgpt import error, util
from robotgpt.robotgpt_response import RobotGPTResponse

from robotgpt import api_requestor
from robotgpt.api_resource import APIResource

MAX_TIMEOUT = 20


class EngineAPIResource(APIResource):
    plain_old_data = False

    def __init__(self, engine: Optional[str] = None, **kwargs):
        super().__init__(engine=engine, **kwargs)


    @classmethod
    def __prepare_create_request(
        cls,
        api_token=None,
        api_url=None,
        **params,
    ):
        model = params.get("model", None)
        timeout = params.pop("timeout", None)
        stream = params.get("stream", False)
        headers = params.pop("headers", None)
        request_timeout = params.pop("request_timeout", None)

        if timeout is None:
            # No special timeout handling
            pass
        elif timeout > 0:
            # API only supports timeouts up to MAX_TIMEOUT
            params["timeout"] = min(timeout, MAX_TIMEOUT)
            timeout = (timeout - params["timeout"]) or None
        elif timeout == 0:
            params["timeout"] = MAX_TIMEOUT

        requestor = api_requestor.APIRequestor(
            api_token,
            api_url=api_url,
            model=model
        )
        return (
            timeout,
            stream,
            headers,
            request_timeout,
            requestor,
            api_url,
            params,
        )

    @classmethod
    def create(
        cls,
        api_token=None,
        api_url=None,
        request_id=None,
        **params,
    ):
        (
            timeout,
            stream,
            headers,
            request_timeout,
            requestor,
            url,
            params,
        ) = cls.__prepare_create_request(
            api_token, api_url, **params
        )

        response, _, api_token = requestor.request(
            "post",
            params=params,
            headers=headers,
            stream=stream,
            request_id=request_id,
            request_timeout=request_timeout,
        )

        if stream:
            # must be an iterator
            assert not isinstance(response, RobotGPTResponse)
            return (
                util.convert_to_openai_object(
                    line,
                    api_token,
                    plain_old_data=cls.plain_old_data,
                )
                for line in response
            )
        else:
            obj = util.convert_to_openai_object(
                response,
                api_token,
                plain_old_data=cls.plain_old_data,
            )

            if timeout is not None:
                obj.wait(timeout=timeout or None)

        return obj

    @classmethod
    async def acreate(
        cls,
        api_token=None,
        api_url=None,
        request_id=None,
        **params,
    ):
        (
            timeout,
            stream,
            headers,
            request_timeout,
            requestor,
            url,
            params,
        ) = cls.__prepare_create_request(
            api_token, api_url, **params
        )
        response, _, api_token = await requestor.arequest(
            "post",
            url,
            params=params,
            headers=headers,
            stream=stream,
            request_id=request_id,
            request_timeout=request_timeout,
        )

        if stream:
            # must be an iterator
            assert not isinstance(response, RobotGPTResponse)
            return (
                util.convert_to_openai_object(
                    line,
                    api_url,
                    plain_old_data=cls.plain_old_data,
                )
                async for line in response
            )
        else:
            obj = util.convert_to_openai_object(
                response,
                api_token,
                plain_old_data=cls.plain_old_data,
            )

            if timeout is not None:
                await obj.await_(timeout=timeout or None)

        return obj

    def wait(self, timeout=None):
        start = time.time()
        while self.status != "complete":
            self.timeout = (
                min(timeout + start - time.time(), MAX_TIMEOUT)
                if timeout is not None
                else MAX_TIMEOUT
            )
            if self.timeout < 0:
                del self.timeout
                break
            self.refresh()
        return self

    async def await_(self, timeout=None):
        """Async version of `EngineApiResource.wait`"""
        start = time.time()
        while self.status != "complete":
            self.timeout = (
                min(timeout + start - time.time(), MAX_TIMEOUT)
                if timeout is not None
                else MAX_TIMEOUT
            )
            if self.timeout < 0:
                del self.timeout
                break
            await self.arefresh()
        return self

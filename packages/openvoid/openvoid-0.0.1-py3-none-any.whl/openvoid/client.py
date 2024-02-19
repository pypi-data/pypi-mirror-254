import os
import posixpath
import time
from json import JSONDecodeError
from typing import Any, Dict, Iterable, Iterator, List, Optional, Union

from httpx import Client, ConnectError, HTTPTransport, RequestError, Response

from openvoid.client_base import ClientBase
from openvoid.constants import ENDPOINT
from openvoid.exceptions import (
    OpenVoidAPIException,
    OpenVoidAPIStatusException,
    OpenVoidConnectionException,
    OpenVoidException,
)
from openvoid.models.chat_completion import (
    ChatCompletionResponse,
    ChatCompletionStreamResponse,
    ChatMessage,
)
from openvoid.models.models import ModelList


class OpenVoidClient(ClientBase):
    """
    Synchronous wrapper around the async client
    """

    def __init__(
        self,
        api_key: Optional[str] = os.environ.get("OPENVOID_API_KEY", None),
        endpoint: str = ENDPOINT,
        max_retries: int = 5,
        timeout: int = 120,
    ):
        super().__init__(endpoint, api_key, max_retries, timeout)

        self._client = Client(
            follow_redirects=True,
            timeout=self._timeout,
            transport=HTTPTransport(retries=self._max_retries))

    def __del__(self) -> None:
        self._client.close()

    def _request(
        self,
        method: str,
        json: Dict[str, Any],
        path: str,
        stream: bool = False,
        attempt: int = 1,
    ) -> Iterator[Dict[str, Any]]:
        accept_header = "text/event-stream" if stream else "application/json"
        headers = {
            "Accept": accept_header,
            "User-Agent": f"openvoid-client-python/{self._version}",
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }

        url = posixpath.join(self._endpoint, path)

        self._logger.debug(f"Sending request: {method} {url} {json}")

        response: Response

        try:
            if stream:
                with self._client.stream(
                    method,
                    url,
                    headers=headers,
                    json=json,
                ) as response:
                    self._check_streaming_response(response)

                    for line in response.iter_lines():
                        json_streamed_response = self._process_line(line)
                        if json_streamed_response:
                            yield json_streamed_response

            else:
                response = self._client.request(
                    method,
                    url,
                    headers=headers,
                    json=json,
                )

                yield self._check_response(response)

        except ConnectError as e:
            raise OpenVoidConnectionException(str(e)) from e
        except RequestError as e:
            raise OpenVoidException(
                f"Unexpected exception ({e.__class__.__name__}): {e}"
            ) from e
        except JSONDecodeError as e:
            raise OpenVoidAPIException.from_response(
                response,
                message=f"Failed to decode json body: {response.text}",
            ) from e
        except OpenVoidAPIStatusException as e:
            attempt += 1
            if attempt > self._max_retries:
                raise OpenVoidAPIStatusException.from_response(
                    response, message=str(e)
                ) from e
            backoff = 2.0**attempt  # exponential backoff
            time.sleep(backoff)

            # Retry as a generator
            for r in self._request(method, json, path, stream=stream, attempt=attempt):
                yield r

    def chat(
        self,
        model: str,
        messages: List[ChatMessage],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_p: Optional[float] = None,
    ) -> ChatCompletionResponse:
        """A chat endpoint that returns a single response.

        Args:
            model (str): model the name of the model to chat with, e.g. prox
            messages (List[ChatMessage]): messages an array of messages to chat with, e.g.
                [{role: 'user', content: 'What is SQL Injection?'}]
            temperature (Optional[float], optional): temperature the temperature to use for sampling, e.g. 0.5.
            max_tokens (Optional[int], optional): the maximum number of tokens to generate, e.g. 100. Defaults to None.
            top_p (Optional[float], optional): the cumulative probability of tokens to generate, e.g. 0.9.
            Defaults to None.
            random_seed (Optional[int], optional): the random seed to use for sampling, e.g. 42. Defaults to None.
            safe_mode (bool, optional): deprecated, use safe_prompt instead. Defaults to False.
            safe_prompt (bool, optional): whether to use safe prompt, e.g. true. Defaults to False.

        Returns:
            ChatCompletionResponse: a response object containing the generated text.
        """
        request = self._make_chat_request(
            model,
            messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            stream=False,
        )

        single_response = self._request("post", request, "v1/chat/completions")

        for response in single_response:
            return ChatCompletionResponse(**response)

        raise OpenVoidException("No response received")

    def chat_stream(
        self,
        model: str,
        messages: List[ChatMessage],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_p: Optional[float] = None,
    ) -> Iterable[ChatCompletionStreamResponse]:
        """A chat endpoint that streams responses.

        Args:
            model (str): model the name of the model to chat with, e.g. prox
            messages (List[ChatMessage]): messages an array of messages to chat with, e.g.
                [{role: 'user', content: 'What is SQL Injection?'}]
            temperature (Optional[float], optional): temperature the temperature to use for sampling, e.g. 0.5.
            max_tokens (Optional[int], optional): the maximum number of tokens to generate, e.g. 100. Defaults to None.
            top_p (Optional[float], optional): the cumulative probability of tokens to generate, e.g. 0.9.
            Defaults to None.
            random_seed (Optional[int], optional): the random seed to use for sampling, e.g. 42. Defaults to None.
            safe_mode (bool, optional): deprecated, use safe_prompt instead. Defaults to False.
            safe_prompt (bool, optional): whether to use safe prompt, e.g. true. Defaults to False.

        Returns:
             Iterable[ChatCompletionStreamResponse]:
                A generator that yields ChatCompletionStreamResponse objects.
        """
        request = self._make_chat_request(
            model,
            messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            stream=True,
        )

        response = self._request("post", request, "v1/chat/completions", stream=True)

        for json_streamed_response in response:
            yield ChatCompletionStreamResponse(**json_streamed_response)

    def list_models(self) -> ModelList:
        """Returns a list of the available models

        Returns:
            ModelList: A response object containing the list of models.
        """
        singleton_response = self._request("get", {}, "v1/models")

        for response in singleton_response:
            return ModelList(**response)

        raise OpenVoidException("No response received")

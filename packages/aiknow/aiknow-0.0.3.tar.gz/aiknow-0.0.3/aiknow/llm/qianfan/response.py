from typing import Coroutine, Iterator
import qianfan

from ..chat import (
    ChatResponse,
    ChatTokenUsage,
    StreamedChatResponse,
    AsyncStreamedChatResponse,
)


class QianfanStreamedChatResponse(StreamedChatResponse):
    def __init__(self, iterator: Iterator[qianfan.QfResponse]) -> None:
        # Qianfan's streamed response as an iterator
        self._iterator = iterator

    def generate_chat_response(self) -> ChatResponse:
        # Get the next chunk
        chunk = next(self._iterator)

        # Create a ChatResponse
        response = ChatResponse(
            content=chunk["result"],
            token_usage=ChatTokenUsage(
                prompt_tokens=chunk["usage"]["prompt_tokens"],
                completion_tokens=chunk["usage"]["completion_tokens"],
                total_tokens=chunk["usage"]["total_tokens"],
            ),
        )

        return response


class AsyncQianfanStreamedChatResponse(AsyncStreamedChatResponse):
    def __init__(self, stream: Coroutine) -> None:
        # Qianfan's streamed response as an iterator
        self._stream = stream

    async def generate_chat_response_async(self) -> ChatResponse:
        # Get the next chunk
        chunk = await anext(self._stream)

        # Create a ChatResponse
        response = ChatResponse(
            content=chunk["result"],
            token_usage=ChatTokenUsage(
                prompt_tokens=chunk["usage"]["prompt_tokens"],
                completion_tokens=chunk["usage"]["completion_tokens"],
                total_tokens=chunk["usage"]["total_tokens"],
            ),
        )

        return response

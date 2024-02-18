from typing import Optional
from pydantic import BaseModel
from abc import ABC, abstractmethod
from collections.abc import Generator, AsyncGenerator


class ChatTokenUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatResponse(BaseModel):
    content: str
    token_usage: Optional[ChatTokenUsage]


class StreamedChatResponse(Generator[ChatResponse, None, None], ABC):
    @abstractmethod
    def generate_chat_response(self) -> ChatResponse:
        """Generate the next chat response.
        Raise `StopIteration` if there are no more responses.

        Returns
        -------
        ChatResponse
            The next chat response.
        """

        pass

    def send(self, value) -> ChatResponse:
        """Send a value into the generator.
        Return next yielded value or raise StopIteration.
        """

        return self.generate_chat_response()

    def throw(self, typ, val=None, tb=None):
        """Raise an exception in the generator.
        Return next yielded value or raise StopIteration.

        Notes
        -----
        The implementation of this method is taken from the CPython source code:
        https://github.com/python/cpython/blob/d5d3249e8a37936d32266fa06ac20017307a1f70/Lib/_collections_abc.py#L309
        """

        if val is None:
            if tb is None:
                raise typ
            val = typ()
        if tb is not None:
            val = val.with_traceback(tb)
        raise val


class AsyncStreamedChatResponse(AsyncGenerator[ChatResponse, None, None], ABC):
    @abstractmethod
    async def generate_chat_response_async(self) -> ChatResponse:
        """Generate the next chat response asynchronously.
        Raise `StopAsyncIteration` if there are no more responses.

        Returns
        -------
        ChatResponse
            The next chat response.
        """

        pass

    async def asend(self, value) -> ChatResponse:
        """Send a value into the asynchronous generator.
        Return next yielded value or raise StopAsyncIteration.
        """

        return await self.generate_chat_response_async()

    async def athrow(self, typ, val=None, tb=None):
        """Raise an exception in the asynchronous generator.
        Return next yielded value or raise StopAsyncIteration.

        Notes
        -----
        The implementation of this method is taken from the CPython source code:
        https://github.com/python/cpython/blob/d5d3249e8a37936d32266fa06ac20017307a1f70/Lib/_collections_abc.py#L309
        """

        if val is None:
            if tb is None:
                raise typ
            val = typ()
        if tb is not None:
            val = val.with_traceback(tb)
        raise val

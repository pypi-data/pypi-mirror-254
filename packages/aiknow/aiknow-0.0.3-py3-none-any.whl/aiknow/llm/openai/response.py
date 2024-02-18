import openai

from ..chat import ChatResponse, StreamedChatResponse, AsyncStreamedChatResponse


class OpenAIStreamedChatResponse(StreamedChatResponse):
    def __init__(self, stream: openai.Stream) -> None:
        # Store OpenAI's stream
        self._stream = stream

    def generate_chat_response(self) -> ChatResponse:
        # Get the next chunk
        chunk = next(self._stream)

        # Extract the content
        content = chunk.choices[0].delta.content

        if content is not None:
            return ChatResponse(
                content=content,
                token_usage=None,
            )
        else:
            raise StopIteration


class AsyncOpenAIStreamedChatResponse(AsyncStreamedChatResponse):
    def __init__(self, stream: openai.AsyncStream) -> None:
        # Store OpenAI's async stream
        self._stream = stream

    async def generate_chat_response_async(self) -> ChatResponse:
        # Get the next chunk
        chunk = await anext(self._stream)

        # Extract the content
        content = chunk.choices[0].delta.content

        if content is not None:
            return ChatResponse(
                content=content,
                token_usage=None,
            )
        else:
            raise StopAsyncIteration

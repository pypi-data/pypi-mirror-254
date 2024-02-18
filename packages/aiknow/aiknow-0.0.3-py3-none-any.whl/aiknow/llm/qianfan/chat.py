from typing import Optional
import qianfan

from .auth import QianfanAuth
from ..chat import (
    ChatModel,
    ChatMessage,
    ChatResponse,
    ChatTokenUsage,
    StreamedChatResponse,
    UserChatMessage,
)
from .response import QianfanStreamedChatResponse, AsyncQianfanStreamedChatResponse


class QianfanChatModel(ChatModel):
    auth: Optional[QianfanAuth] = None

    def get_complete_response(
        self,
        messages: str | ChatMessage | list[ChatMessage],
    ) -> ChatResponse:
        # Convert to a list of messages
        messages = self._convert_to_chat_message_list(messages)

        # Call the API
        response = qianfan.ChatCompletion(
            model=self.name,
            ak=self.auth.access_key,
            sk=self.auth.secret_key,
        ).do(
            # Set the profile via the system attribute
            system=self.profile,
            messages=list(
                map(
                    lambda message: dict(
                        role=message.role.value,
                        content=message.content,
                    ),
                    messages,
                )
            ),
            temperature=self.temperature,
        )

        # Convert a ChatResponse
        response = ChatResponse(
            content=response["result"],
            token_usage=ChatTokenUsage(
                prompt_tokens=response["usage"]["prompt_tokens"],
                completion_tokens=response["usage"]["completion_tokens"],
                total_tokens=response["usage"]["total_tokens"],
            ),
        )

        return response

    def get_streamed_response(
        self,
        messages: str | ChatMessage | list[ChatMessage],
    ) -> StreamedChatResponse:
        # Convert to a list of messages
        messages = self._convert_to_chat_message_list(messages)

        # Call the API
        iterator = qianfan.ChatCompletion(
            model=self.name,
            ak=self.auth.access_key,
            sk=self.auth.secret_key,
        ).do(
            # Set the profile via the system attribute
            system=self.profile,
            messages=list(
                map(
                    lambda message: dict(
                        role=message.role.value,
                        content=message.content,
                    ),
                    messages,
                )
            ),
            temperature=self.temperature,
            # Enable streaming
            stream=True,
        )

        # Convert to streamed response
        streamed_response = QianfanStreamedChatResponse(iterator)

        return streamed_response

    async def get_complete_response_async(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> ChatResponse:
        # Convert to a list of messages
        messages = self._convert_to_chat_message_list(messages)

        # Call the API
        response = await qianfan.ChatCompletion(
            model=self.name,
            ak=self.auth.access_key,
            sk=self.auth.secret_key,
        ).ado(
            # Set the profile via the system attribute
            system=self.profile,
            messages=list(
                map(
                    lambda message: dict(
                        role=message.role.value,
                        content=message.content,
                    ),
                    messages,
                )
            ),
            temperature=self.temperature,
        )

        # Convert a ChatResponse
        response = ChatResponse(
            content=response["result"],
            token_usage=ChatTokenUsage(
                prompt_tokens=response["usage"]["prompt_tokens"],
                completion_tokens=response["usage"]["completion_tokens"],
                total_tokens=response["usage"]["total_tokens"],
            ),
        )

        return response

    async def get_streamed_response_async(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> AsyncQianfanStreamedChatResponse:
        # Convert to a list of messages
        messages = self._convert_to_chat_message_list(messages)

        # Call the API
        stream = await qianfan.ChatCompletion(
            model=self.name,
            ak=self.auth.access_key,
            sk=self.auth.secret_key,
        ).ado(
            # Set the profile via the system attribute
            system=self.profile,
            messages=list(
                map(
                    lambda message: dict(
                        role=message.role.value,
                        content=message.content,
                    ),
                    messages,
                )
            ),
            temperature=self.temperature,
            # Enable streaming
            stream=True,
        )

        # Convert to streamed response
        streamed_response = AsyncQianfanStreamedChatResponse(stream)

        return streamed_response

from typing import Optional
from openai import OpenAI, AsyncOpenAI

from .auth import OpenAIAuth
from ..chat import (
    ChatModel,
    ChatMessage,
    UserChatMessage,
    ChatResponse,
    ChatTokenUsage,
)
from .response import OpenAIStreamedChatResponse, AsyncOpenAIStreamedChatResponse


class OpenAIChatModel(ChatModel):
    auth: Optional[OpenAIAuth] = None

    def get_complete_response(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> ChatResponse:
        # Prepare messages
        messages = self._prepare_messages(messages)

        # Call the API
        response = OpenAI(api_key=self.auth.api_key).chat.completions.create(
            model=self.name,
            messages=messages,
            temperature=self.temperature,
        )

        # Convert a ChatResponse
        response = ChatResponse(
            content=response.choices[0].message.content,
            token_usage=ChatTokenUsage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            ),
        )

        return response

    def get_streamed_response(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> OpenAIStreamedChatResponse:
        # Prepare messages
        messages = self._prepare_messages(messages)

        # Call the API and get the stream
        stream = OpenAI(api_key=self.auth.api_key).chat.completions.create(
            model=self.name,
            messages=messages,
            temperature=self.temperature,
            # Enable streaming
            stream=True,
        )

        # Create a streamed response
        streamed_response = OpenAIStreamedChatResponse(stream)

        return streamed_response

    async def get_complete_response_async(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> ChatResponse:
        # Prepare messages
        messages = self._prepare_messages(messages)

        # Call the API
        response = await AsyncOpenAI(api_key=self.auth.api_key).chat.completions.create(
            model=self.name,
            messages=messages,
            temperature=self.temperature,
        )

        # Convert a ChatResponse
        response = ChatResponse(
            content=response.choices[0].message.content,
            token_usage=ChatTokenUsage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            ),
        )

        return response

    async def get_streamed_response_async(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> AsyncOpenAIStreamedChatResponse:
        # Prepare messages
        messages = self._prepare_messages(messages)

        # Call the API
        stream = await AsyncOpenAI(api_key=self.auth.api_key).chat.completions.create(
            model=self.name,
            messages=messages,
            temperature=self.temperature,
            # Enable streaming
            stream=True,
        )

        # Create a streamed response
        streamed_response = AsyncOpenAIStreamedChatResponse(stream)

        return streamed_response

    def _prepare_messages(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> list[dict[str, str]]:
        """Prepare messages for the API.

        Parameters
        ----------
        messages : str | UserChatMessage | list[ChatMessage]
            One of the following:
            - User message content.
            - A single user message.
            - A list of messages of the user and the assistant.

        Returns
        -------
        list[dict[str, str]]
            Messages to be sent to the API.
        """

        # Convert a single message to a list
        messages = self._convert_to_chat_message_list(messages)

        # Prepare messages
        messages = list(
            map(
                lambda message: dict(
                    role=message.role.value,
                    content=message.content,
                ),
                messages,
            )
        )

        # Add a system message in the front if the profile is set
        system_message = self._create_system_message()
        if system_message is not None:
            messages.insert(0, system_message)

        return messages

    def _create_system_message(self) -> Optional[dict[str, str]]:
        """Create a system message from the profile.

        Returns
        -------
        Optional[dict[str, str]]
            A system message.
        """

        # No system message is needed if the profile is not set
        if self.profile is None:
            return None

        # Create a system message
        return dict(
            role="system",
            content=self.profile,
        )

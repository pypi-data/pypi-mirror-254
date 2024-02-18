from typing import Optional, Any
from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from ..auth import LLMAuth
from .message import ChatMessage, UserChatMessage
from .response import ChatResponse, StreamedChatResponse


class ChatModel(BaseModel, ABC):
    name: str
    profile: Optional[str] = None
    temperature: float = Field(gt=0, lt=1, default=0.9)
    auth: Optional[LLMAuth] = None

    @abstractmethod
    def get_complete_response(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> ChatResponse:
        """Get a complete response from the LLM chat model.

        Parameters
        ----------
        messages : str | ChatMessage | list[ChatMessage]
            One of the following:
            - User message content.
            - A single user message.
            - A list of messages of the user and the assistant.

        Returns
        -------
        ChatResponse
            A response from the LLM chat model.
        """

        pass

    @abstractmethod
    def get_streamed_response(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> StreamedChatResponse:
        """Get a streamed response from the LLM chat model.

        Parameters
        ----------
        messages : str | ChatMessage | list[ChatMessage]
            One of the following:
            - User message content.
            - A single user message.
            - A list of messages of the user and the assistant.

        Returns
        -------
        StreamedChatResponse
            A streamed response from the LLM chat model.
        """
        pass

    @abstractmethod
    async def get_complete_response_async(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> ChatResponse:
        """Get a complete response from the LLM chat model asynchronously.

        Parameters
        ----------
        messages: str | UserChatMessage | list[ChatMessage]
            One of the following:
            - User message content.
            - A single user message.
            - A list of messages of the user and the assistant.

        Returns
        -------
        ChatResponse
            A response from the LLM chat model.
        """

        pass

    @abstractmethod
    async def get_streamed_response_async(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> StreamedChatResponse:
        """Get a streamed response from the LLM chat model asynchronously.

        Parameters
        ----------
        messages: str | UserChatMessage | list[ChatMessage]
            One of the following:
            - User message content.
            - A single user message.
            - A list of messages of the user and the assistant.

        Returns
        -------
        StreamedChatResponse
            A streamed response from the LLM chat model.
        """

        pass

    def model_post_init(self, __context: Any) -> None:
        # Call method of super class
        super().model_post_init(__context)

        # Initialize auth from environment variables
        # if it is not provided
        if self.auth is None:

            # Get the runtime type of the auth
            types = self.model_fields.get("auth").annotation.__args__
            try:
                auth_type = next(filter(lambda x: x != type(None), types))
            except StopIteration:
                raise ValueError("Failed to get the runtime type of the auth")

            # Initialize the auth
            self.auth = auth_type()

    @staticmethod
    def _convert_to_chat_message_list(
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> list[ChatMessage]:
        """Convert a single user message or a string to a list of messages
        if the input `messages` is actually a single message.

        Parameters
        ----------
        messages : str | UserChatMessage | list[ChatMessage]
            One of the following:
            - User message content.
            - A single user message.
            - A list of messages of the user and the assistant.

        Returns
        -------
        list[ChatMessage]
            A list of messages.
        """

        # Convert user message content to a list of messages
        if isinstance(messages, str):
            messages = [UserChatMessage(content=messages)]

        # Convert a single user message to a list
        if isinstance(messages, UserChatMessage):
            messages = [messages]

        return messages

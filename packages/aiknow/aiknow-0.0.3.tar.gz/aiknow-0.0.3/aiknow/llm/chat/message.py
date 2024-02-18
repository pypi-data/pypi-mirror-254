from enum import StrEnum
from pydantic import BaseModel, ConfigDict


class ChatRole(StrEnum):
    USER = "user"
    ASSISTANT = "assistant"


class ChatMessage(BaseModel):
    role: ChatRole
    content: str

    model_config = ConfigDict(
        frozen=True,
    )


class UserChatMessage(ChatMessage):
    role: ChatRole = ChatRole.USER


class AssistantChatMessage(ChatMessage):
    role: ChatRole = ChatRole.ASSISTANT

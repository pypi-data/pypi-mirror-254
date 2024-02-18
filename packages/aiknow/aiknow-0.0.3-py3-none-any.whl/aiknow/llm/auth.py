from abc import ABC
from pydantic_settings import BaseSettings


class LLMAuth(BaseSettings, ABC):
    """Base class for LLM authentication."""

    pass

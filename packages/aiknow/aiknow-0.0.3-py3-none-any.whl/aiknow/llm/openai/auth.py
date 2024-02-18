from pydantic import Field
from ..auth import LLMAuth


class OpenAIAuth(LLMAuth):
    api_key: str = Field(alias="OPENAI_API_KEY")

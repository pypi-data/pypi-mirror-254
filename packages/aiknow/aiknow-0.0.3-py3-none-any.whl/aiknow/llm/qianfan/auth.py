from pydantic import Field
from ..auth import LLMAuth


class QianfanAuth(LLMAuth):
    access_key: str = Field(alias="QIANFAN_ACCESS_KEY")
    secret_key: str = Field(alias="QIANFAN_SECRET_KEY")

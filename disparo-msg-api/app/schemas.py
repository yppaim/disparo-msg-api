from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class MessageRequest(BaseModel):
    recipient: str = Field(..., min_length=3, max_length=160)
    message: str = Field(..., min_length=1, max_length=1000)
    channel: Literal["sms", "whatsapp", "email"] = "email"

    @field_validator("recipient")
    @classmethod
    def validate_recipient(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("O destinatário não pode ficar vazio.")

        return value


class MessageResponse(BaseModel):
    id: str
    recipient: str
    message: str
    channel: str
    status: Literal["sent", "failed"]
    created_at: datetime

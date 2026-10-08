from datetime import datetime, timezone
from uuid import uuid4

from app.schemas import MessageRequest, MessageResponse


class MessageService:
    """Serviço de envio simulado.

    Em produção, este componente pode ser substituído por um adapter
    para Twilio, WhatsApp Business, SendGrid, AWS SES etc.
    """

    def __init__(self):
        self.messages: dict[str, MessageResponse] = {}

    def send(self, payload: MessageRequest) -> MessageResponse:
        message = MessageResponse(
            id=str(uuid4()),
            recipient=payload.recipient,
            message=payload.message,
            channel=payload.channel,
            status="sent",
            created_at=datetime.now(timezone.utc),
        )

        self.messages[message.id] = message
        return message

    def get(self, message_id: str) -> MessageResponse | None:
        return self.messages.get(message_id)

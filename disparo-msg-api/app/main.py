from fastapi import Depends, FastAPI, Header, HTTPException, status

from app.schemas import MessageRequest, MessageResponse
from app.service import MessageService

app = FastAPI(
    title="Messaging API",
    description=(
        "API de notificações para portfólio. "
        "O provedor de envio é simulado para desenvolvimento e testes."
    ),
    version="1.0.0",
)

service = MessageService()


def authenticate(x_api_key: str | None = Header(default=None)):
    if x_api_key != "portfolio-dev-key":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key inválida.",
        )


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}


@app.post(
    "/messages",
    response_model=MessageResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Messages"],
    dependencies=[Depends(authenticate)],
)
def send_message(payload: MessageRequest):
    return service.send(payload)


@app.get(
    "/messages/{message_id}",
    response_model=MessageResponse,
    tags=["Messages"],
    dependencies=[Depends(authenticate)],
)
def get_message(message_id: str):
    message = service.get(message_id)

    if not message:
        raise HTTPException(status_code=404, detail="Mensagem não encontrada.")

    return message

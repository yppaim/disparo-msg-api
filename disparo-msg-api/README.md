# 📩 Messaging API

API REST de notificações desenvolvida em **Python + FastAPI**, criada como projeto de portfólio para demonstrar construção, documentação, autenticação, validação e testes de uma API.

> **Importante:** o projeto utiliza um provedor de envio simulado. Ele não dispara mensagens reais para terceiros. Isso permite estudar a arquitetura da solução sem configurar um serviço externo ou enviar mensagens indesejadas.

## 🎯 Objetivo

A API representa um serviço que recebe solicitações de envio de mensagens e registra o resultado.

Arquitetura:

```text
Cliente
   │
   │ HTTP + API Key
   ▼
┌──────────────────────┐
│     FastAPI API      │
├──────────────────────┤
│ Autenticação         │
│ Validação            │
│ Service Layer        │
└──────────┬───────────┘
           │
           ▼
   Simulated Provider
           │
           ▼
     Message Store
```

O provedor simulado foi separado em uma camada de serviço para facilitar uma futura integração com serviços como Twilio, WhatsApp Business, SendGrid ou AWS SES.

## 🧰 Tecnologias

- Python 3.12+
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- Docker
- OpenAPI / Swagger

## ✨ Funcionalidades

- API REST
- API Key
- Validação de payload
- Envio simulado
- Consulta de mensagem por ID
- Health check
- Documentação automática OpenAPI
- Testes automatizados
- Docker
- Arquitetura separada em rotas, schemas e service layer

## 📁 Estrutura

```text
messaging-api-portfolio/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── service.py
├── tests/
│   └── test_messages.py
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🚀 Executando localmente

### 1. Criar ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Iniciar API

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

```text
http://localhost:8000
```

## 📚 Swagger

A documentação interativa é gerada automaticamente pelo FastAPI.

Abra:

```text
http://localhost:8000/docs
```

Também existe a documentação alternativa:

```text
http://localhost:8000/redoc
```

## 🔐 Autenticação

Os endpoints de mensagens exigem o header:

```http
X-API-Key: portfolio-dev-key
```

> Em um projeto real, a chave deve ficar em variável de ambiente ou em um secret manager. A chave presente neste exemplo é apenas uma credencial fictícia para desenvolvimento.

## 🔌 Endpoints

### GET `/health`

Verifica se a API está funcionando.

Resposta:

```json
{
  "status": "ok"
}
```

### POST `/messages`

Envia uma mensagem de forma simulada.

Header:

```http
X-API-Key: portfolio-dev-key
```

Body:

```json
{
  "recipient": "cliente@example.com",
  "message": "Seu pedido foi confirmado.",
  "channel": "email"
}
```

Resposta:

```json
{
  "id": "8b8a2f5d-...",
  "recipient": "cliente@example.com",
  "message": "Seu pedido foi confirmado.",
  "channel": "email",
  "status": "sent",
  "created_at": "2026-10-08T15:00:00Z"
}
```

### GET `/messages/{message_id}`

Consulta uma mensagem pelo ID.

Header:

```http
X-API-Key: portfolio-dev-key
```

## 🧪 Testes

Execute:

```bash
pytest -v
```

Os testes verificam:

- health check;
- envio de mensagem;
- autenticação;
- validação de dados.

## 🐳 Docker

Construir e executar:

```bash
docker compose up --build
```

Depois acesse:

```text
http://localhost:8000/docs
```

## 🧠 Decisões de arquitetura

### FastAPI

Foi escolhido por oferecer:

- alta produtividade;
- validação com Pydantic;
- documentação OpenAPI automática;
- excelente suporte a APIs REST;
- facilidade para testes.

### Service Layer

A lógica de envio está em `app/service.py`, separada das rotas.

Isso permite trocar:

```text
Simulated Provider
```

por:

```text
Twilio
WhatsApp Business
SendGrid
AWS SES
```

sem precisar reescrever toda a API.

### Armazenamento

O projeto usa memória RAM propositalmente para manter o exemplo pequeno.

Em uma aplicação real, poderia ser:

```text
FastAPI
   ↓
PostgreSQL
   ↓
Redis / RabbitMQ
   ↓
Worker
   ↓
Provider de mensagens
```

## 🚀 Evoluções recomendadas

Para transformar este projeto em uma API mais próxima de produção:

1. Adicionar PostgreSQL.
2. Criar tabela de mensagens.
3. Implementar fila com Redis/RabbitMQ.
4. Criar worker assíncrono.
5. Integrar um provedor transacional real.
6. Adicionar JWT/OAuth2.
7. Implementar rate limiting.
8. Adicionar logs estruturados.
9. Criar CI/CD com GitHub Actions.
10. Adicionar métricas e observabilidade.

## 💼 O que este projeto demonstra no portfólio

```text
Python
   ↓
FastAPI
   ↓
REST API
   ↓
OpenAPI
   ↓
Authentication
   ↓
Validation
   ↓
Testing
   ↓
Docker
   ↓
Arquitetura modular
```

## 📄 Licença

MIT

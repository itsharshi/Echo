# Echo Backend

FastAPI service for Echo's audio processing, voice cloning, and API layer.

## Setup

Requires Postgres and MinIO running locally — see [../infra/README.md](../infra/README.md).

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
cp .env.example .env
```

## Run locally

```bash
./.venv/bin/uvicorn main:app --reload --port 8010
```

> Note: port 8000 may already be in use by another local service (e.g. Docker Desktop) on some machines — 8010 is used to avoid that conflict. Adjust `NEXT_PUBLIC_API_URL` in `frontend/.env.local` if you change this.

Health check: `GET http://localhost:8010/health` → `{"status": "ok"}`

Interactive API docs: `http://localhost:8010/docs`

## API

| Endpoint | Description |
|---|---|
| `POST /people` | Create a person `{ "name": string }` |
| `GET /people/{id}` | Fetch a person |
| `GET /people` | List all people |
| `POST /people/{id}/recordings` | Upload an audio recording (multipart `file`) for a person |
| `GET /people/{id}/recordings` | List a person's recordings |
| `GET /recordings/{id}/audio` | Stream a recording's audio (playback) |

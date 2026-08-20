# Echo Backend

FastAPI service for Echo's audio processing, voice cloning, and API layer.

## Setup

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

## Run locally

```bash
./.venv/bin/uvicorn main:app --reload --port 8000
```

Health check: `GET http://localhost:8000/health` → `{"status": "ok"}`

# Echo

AI-powered personality, memory, and voice preservation platform.

Phase 1 focuses on proving zero-shot voice cloning end-to-end: capture a voice sample, clone it using an open-source model, and play back arbitrary text in that voice.

## Project Structure

```
Echo/
├── backend/    FastAPI service (audio processing, voice cloning, API)
├── frontend/   Next.js web app (capture flow, playback UI)
├── infra/      Deployment configs (Docker, CI/CD, environment setup)
└── planning/   Project tickets and roadmap
```

## Getting Started

1. Start local infra (Postgres + MinIO) — see [infra/README.md](infra/README.md)
2. Start the backend — see [backend/README.md](backend/README.md)
3. Start the frontend — see [frontend/README.md](frontend/README.md)

## What's built so far

- **Person profile** — backend API to create/fetch a person, plus a frontend screen (no login)
- **Audio recording** — record and play back a voice sample in the browser, upload it to the backend
- **Storage** — recordings are saved to MinIO (object storage) with metadata in Postgres

## Status

Phase 1 — Voice Cloning Pipeline (in progress). See [planning/echo_phase1_tickets.csv](planning/echo_phase1_tickets.csv) for the current task list.

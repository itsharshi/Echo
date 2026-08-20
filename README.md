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

See [backend/README.md](backend/README.md) and [frontend/README.md](frontend/README.md) for setup instructions for each service.

## Status

Phase 1 — Voice Cloning Pipeline (in progress). See [planning/echo_phase1_tickets.csv](planning/echo_phase1_tickets.csv) for the current task list.

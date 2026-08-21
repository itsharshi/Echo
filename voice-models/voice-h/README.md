# Harshith's Voice Model Evaluation

Models to test: XTTS-v2 (via `coqui-tts` community fork), GPT-SoVITS, and Hinglish-TTS ([harrrshall/hinglish-tts](https://github.com/harrrshall/hinglish-tts)).

Set up your own venv here (`.venv/`) so it doesn't clash with `backend/.venv`. Using Python 3.11 (via `/opt/homebrew/bin/python3.11`), not the system Python 3.14 — most ML packages (torch, transformers, etc.) don't have mature wheels for 3.14 yet.

Put reference audio, test scripts, and outputs in `results/` — see `../README.md` for what to capture per model.

## Status: Hinglish-TTS deferred — needs a CUDA GPU

Checked the actual repo (`harrrshall/hinglish-tts`) before installing anything. Its README states **CUDA GPU (≥6GB VRAM) as a prerequisite**, and its `setup.sh` is Ubuntu-only (apt-get, deadsnakes PPA) and compiles `fairseq` from source — fairseq has known build failures on Apple Silicon/ARM. Neither of our M1 Pro laptops has a CUDA GPU, and there's no macOS-specific guidance anywhere in the repo's docs.

**Decision (2026-08-21):** skip Hinglish-TTS for now, start with XTTS-v2 and GPT-SoVITS which both run on CPU/MPS without exotic native-compile dependencies. Revisit Hinglish-TTS later on a rented cloud GPU box if the other models' Hinglish output isn't good enough on its own.

## Order of work

1. ~~Hinglish-TTS~~ — deferred, see above.
2. **XTTS-v2** — in progress.
3. **GPT-SoVITS** — not started.

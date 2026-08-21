# Harshith's Voice Model Evaluation

Models to test: XTTS-v2 (via `coqui-tts` community fork), GPT-SoVITS, and **Hinglish-TTS** ([harrrshall/hinglish-tts](https://github.com/harrrshall/hinglish-tts)) — the purpose-built Hinglish code-switching model. This last one is the most important test given our stated language priority (Hinglish first) — start with it if time is short.

Set up your own venv here (`.venv/`, gitignored) so it doesn't clash with `backend/.venv`.

Put reference audio, test scripts, and outputs in `results/` — see `../README.md` for what to capture per model.

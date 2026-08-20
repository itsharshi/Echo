# Shreya's Voice Model Evaluation

Models to test: F5-TTS, IndexTTS-2, and **AI4Bharat IndicF5** ([AI4Bharat/IndicF5](https://github.com/AI4Bharat/IndicF5)) — the Indian-language base model that Harshith's Hinglish-TTS model builds on. Testing this directly shows what the Hinglish code-switching wrapper adds versus the base model.

Set up your own venv here (`.venv/`, gitignored) so it doesn't clash with `backend/.venv`.

Put reference audio, test scripts, and outputs in `results/` — see `../README.md` for what to capture per model.

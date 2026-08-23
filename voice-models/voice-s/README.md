# Shreya's Voice Model Evaluation

## Result

Tested F5-TTS, IndexTTS-2, AI4Bharat IndicF5, XTTS-v2, and Chatterbox Multilingual. **F5-TTS and IndexTTS-2 did not perform well** (see notes below) and have been dropped, along with IndicF5. Only **XTTS-v2** and **Chatterbox Multilingual** are kept going forward.

| Model | English | Hinglish | Hindi | Verdict |
|---|---|---|---|---|
| **Chatterbox Multilingual** | Good | Good | Good | Works well across all three — best overall |
| **XTTS-v2** | Good | Weak | Good | Works well for English and Hindi only; struggles with Hinglish code-switching |
| ~~F5-TTS~~ | — | — | — | Dropped — see notes |
| ~~IndexTTS-2~~ | — | — | — | Dropped — see notes |
| ~~IndicF5~~ | — | — | — | Dropped, not evaluated further |

### Why F5-TTS and IndexTTS-2 were dropped

- **F5-TTS**: multi-sentence `gen_text` (text split into batches by punctuation) silently truncated the output to only the last chunk instead of concatenating all batches — required rewriting prompts as a single continuous sentence per generation as a workaround. Even after that fix, Hindi output ran ~2x longer than English/Hinglish for a comparable amount of text, an inconsistency not seen in the other models.
- **IndexTTS-2**: required its own isolated Python 3.11 venv (`.venv_indextts`) separate from every other model due to `transformers` version conflicts; slow on MPS (~180–300s total inference time per ~10–15s of generated audio, RTF ~23–31x). Removed for setup fragility and speed, on top of not being the preferred model for Hinglish going forward.
- **IndicF5**: gated on Hugging Face (requires manual access request), needed a `torch`/`transformers` downgrade to work around a meta-tensor bug in its bundled F5-TTS-based vocoder loading. Not carried forward once F5-TTS itself was dropped.

## Setup

Each model has its own isolated venv (avoids the cross-model dependency conflicts hit during evaluation):

```bash
cd voice-models/voice-s
.venv_xtts/bin/python run_xtts.py
.venv_chatterbox/bin/python run_chatterbox.py
```

- `chatterbox/` — cloned from [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) (installed via `pip install chatterbox-tts` into `.venv_chatterbox`)
- `run_xtts.py` / `run_chatterbox.py` — generation scripts, one per model, each producing English/Hinglish/Hindi samples from the same reference clip

### Known setup gotchas

- **XTTS-v2** requires `COQUI_TOS_AGREED=1` env var to skip an interactive license prompt that otherwise hangs non-interactive/background runs.
- **Chatterbox** requires `setuptools<81` (newer setuptools removed `pkg_resources`, which a bundled dependency — `resemble-perth`, the watermarking library — imports at load time; without the pin, model loading fails with a confusing `TypeError: 'NoneType' object is not callable`).

## Reference audio

`results/reference_v2.wav` — ~65s clip, transcribed via local Whisper (`base` model) into `results/reference_v2_transcript.txt`. XTTS-v2 and Chatterbox both take the raw reference audio directly (no transcript needed for cloning); the transcript file is kept for reference/reproducibility.

## Results

`results/xtts-v2/` and `results/chatterbox/` each contain `output_en.wav`, `output_hinglish.wav`, `output_hindi.wav`.

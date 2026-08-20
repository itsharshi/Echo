# Voice Models — Evaluation Workspace

This is where we benchmark open-source zero-shot voice cloning models before wiring one into the Echo backend (Step 21 in `planning/echo_phase1_tickets.csv`).

**Priority order for language support:** Hinglish (code-switched Hindi/English) → English → Hindi.

## Structure

- `voice-h/` — Harshith's evaluation workspace
- `voice-s/` — Shreya's evaluation workspace

Each person works independently in their own folder (own scripts, own installed models, own sample outputs) so we're not fighting over the same Python environment. We compare results at the end.

## Split

Six models, split 3/3. Each person gets one **general-purpose** model, one **higher-star general-purpose** model, and shares responsibility for the two **Hindi/Hinglish-specific** models so both of us get first-hand signal on the thing we actually care about most.

| Person | Models to evaluate | Why |
|---|---|---|
| **Harshith** | XTTS-v2, GPT-SoVITS, **Hinglish-TTS (harrrshall/hinglish-tts)** | XTTS-v2 is the only general model with an official Hindi claim; GPT-SoVITS is the highest-starred/most active repo overall; Hinglish-TTS is the only model purpose-built for code-switching — this is the most important test in the whole batch. |
| **Shreya** | F5-TTS, IndexTTS-2, **AI4Bharat IndicF5 (base model)** | F5-TTS and IndexTTS-2 are the top general-purpose contenders by 2026 rankings; IndicF5 is the base model Hinglish-TTS is built on, so testing it directly shows what's inherited vs. what the Hinglish wrapper adds. |

Work independently in your own folder (own scripts, own installed models, own sample outputs) so we're not fighting over the same Python environment. Compare results at the end.

## Shortlist & why

Real GitHub star counts and last-push dates pulled directly via the GitHub API, 2026-08-20/21 (not just narrative claims from articles):

### General-purpose models

| Model | Repo | Stars | License | Actively maintained? | Notes |
|---|---|---|---|---|---|
| **GPT-SoVITS** | [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 61.1k | MIT | Yes (pushed 2 days ago) | Highest-starred voice cloning repo on GitHub and actively maintained. Few-shot cloning from ~1 min of data. Strong on Chinese/Japanese/English; Hindi/Hinglish support unconfirmed — needs direct testing. |
| **XTTS-v2** | [idiap/coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) (community fork; original `coqui-ai/TTS` has 46k stars but hasn't been pushed to since Aug 2024 — Coqui the company shut down) | 2.3k (fork) / 46k (original, dead) | MPL-2.0 | Yes (fork) | Officially supports Hindi + English among 17 languages — the only general-purpose model here with an explicit Hindi claim from the vendor. 6-second reference clips. Code-switching (Hinglish) quality is untested/unofficial. |
| **F5-TTS** | [SWivid/F5-TTS](https://github.com/SWivid/F5-TTS) | 15.1k | MIT | Yes (updated Jul 2026) | Trained on ~100k hours multilingual data. Frequently cited as most natural-sounding zero-shot clone. Hindi is not in the official language list — needs direct testing. |
| **IndexTTS-2** | [index-tts/index-tts](https://github.com/index-tts/index-tts) | 23.2k | Custom (check terms) | Yes (updated Aug 2026) | Newer, frequently ranked top-tier in 2026 comparisons alongside Fish Speech. |

### Hindi/Hinglish-specific models

These exist because none of the general-purpose models above are explicitly trained for code-switching — Hinglish isn't "Hindi + English support," it's mid-sentence mixing with its own grammar, and most general models have never seen that pattern in training.

| Model | Repo | Stars | License | Actively maintained? | Notes |
|---|---|---|---|---|---|
| **Hinglish-TTS** | [harrrshall/hinglish-tts](https://github.com/harrrshall/hinglish-tts) | 26 | Apache-2.0 | Yes (pushed May 2026) | **The one purpose-built option.** Built on IndicF5 with automatic script normalization (Devanagari, Roman-script Hindi, mixed-script, English with Indian named entities all in one call). Reports 4.70/5.0 mean intelligibility on a 30-sentence code-switched eval set. Low star count reflects it being a small, recent, focused project — not a quality signal. This is the model to test first given our stated priority. |
| **AI4Bharat IndicF5** | [AI4Bharat/IndicF5](https://github.com/AI4Bharat/IndicF5) | 127 | Unlicensed on repo (check Hugging Face model card) | Slower-moving (last push Sep 2025) | The base model underneath Hinglish-TTS. Supports 11 Indian languages including Hindi, zero-shot voice cloning from a 3-10s reference clip + transcript. Testing this alongside Hinglish-TTS shows exactly what the code-switching wrapper adds. |

**Also considered, not assigned (high stars but weaker fit):**
- [CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) (60.1k stars) and [babysor/MockingBird](https://github.com/babysor/MockingBird) (36.9k stars) — both huge and well-known, but built on older (SV2TTS-era) architecture generally considered behind current SOTA quality; high star count reflects age/popularity more than current best-in-class output. Skip unless the top 5 disappoint.
- [myshell-ai/OpenVoice](https://github.com/myshell-ai/OpenVoice) (37.2k stars, MIT) — momentum has stalled (last push Apr 2025), dropped in favor of GPT-SoVITS/IndexTTS-2 which are both higher-starred-or-comparable and more actively maintained.
- [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) (32.3k stars) — strong 2026 rankings but license terms are non-standard, check carefully before any commercial use; deprioritized versus MIT-licensed options for now.
- [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) (35.9k stars, Apache-2.0) — newer multilingual/tokenizer-free model, actively maintained, worth a look in a second pass if time allows.
- CosyVoice2 — could not confirm a stable public GitHub repo path/star count during this check; revisit if it comes up again with a clear link.

## Zero-shot cloning confirmed for all 6 — but two need a transcript, not just audio

All 6 shortlisted models do genuine zero-shot voice cloning (no training/fine-tuning required, just a short reference clip):

| Model | Reference clip needed | Also needs a transcript? |
|---|---|---|
| GPT-SoVITS | 5s minimum | No — audio only |
| XTTS-v2 | 3-6s minimum (15-30s recommended) | No — audio only |
| F5-TTS | 3-10s | No — audio only |
| IndexTTS-2 | A few seconds | No — audio only |
| **Hinglish-TTS** | 3-10s | **Yes — exact transcript of the reference clip required** |
| **AI4Bharat IndicF5** | 3-10s | **Yes — exact transcript of the reference clip required** |

**Why this matters for the capture flow:** Hinglish-TTS and IndicF5 (both built around IndicF5) need the reference audio's exact transcript as an input alongside the audio itself — not just the audio file like the other four. If either of these ends up being the winning model, Step 17-18 (phonetic capture script + guided recording screen) needs to capture/store that transcript text alongside each recording, not just the audio. Worth designing the capture screen so the transcript is known upfront (e.g. showing the user the exact sentence to read, so the transcript is just "what was on screen") rather than trying to derive it after the fact.

## What "benchmark" means here

For each model, produce:
1. A cloned sample from a **6-10 second reference clip** in English.
2. The same clone speaking a **Hinglish sentence** (code-switched, e.g. "Mujhe lagta hai ki this is a really good idea, yaar").
3. The same clone speaking a **pure Hindi sentence** (Devanagari script).
4. Note: inference time (seconds), whether it ran on MPS or fell back to CPU, and any setup pain (dependency conflicts, model download size, etc).

Save each model's output audio + notes in a `results/` subfolder inside your own workspace (`voice-h/results/` or `voice-s/results/`) so we can do a listening comparison at the end and fill in Step 15/16 of the task list (test through the app, pick the winner).

## Sources

- [Ultimate Guide - Best Open Source Models for Voice Cloning in 2026](https://www.siliconflow.com/articles/en/best-open-source-models-for-voice-cloning)
- [Best Open Source AI Voice Cloning Tools in 2026 — Resemble AI](https://www.resemble.ai/resources/best-open-source-ai-voice-cloning-tools)
- [F5-TTS is the most realistic open source zero shot voice clone model — Uberduck](https://www.uberduck.ai/post/f5-tts-is-the-most-realistic-open-source-zero-shot-text-to-speech-so-far)
- [Hinglish-TTS (harrrshall/hinglish-tts)](https://github.com/harrrshall/hinglish-tts) — the purpose-built Hinglish code-switching model, assigned to Harshith
- [AI4Bharat/IndicF5](https://github.com/AI4Bharat/IndicF5) — base model underneath Hinglish-TTS, assigned to Shreya
- [IndicF5 on Hugging Face](https://huggingface.co/ai4bharat/IndicF5) — model card and usage details
- GitHub API (star counts, license, last-push date) checked directly, 2026-08-20/21

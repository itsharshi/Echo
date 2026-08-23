import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

device = "mps"
model = ChatterboxMultilingualTTS.from_pretrained(device=device)

ref_audio = "results/reference_v2.wav"

wav = model.generate(
    "This is a test of zero shot voice cloning using Chatterbox Multilingual where we are evaluating how natural and clear the cloned voice sounds when speaking a longer sentence for the Echo project",
    language_id="en",
    audio_prompt_path=ref_audio,
)
ta.save("results/chatterbox/output_en.wav", wav, model.sr)

wav = model.generate(
    "Mujhe lagta hai ki this is a really good idea yaar kyunki hum log is project ko test kar rahe hain taaki pata chale ki voice cloning kitni acchi kaam karti hai",
    language_id="en",
    audio_prompt_path=ref_audio,
)
ta.save("results/chatterbox/output_hinglish.wav", wav, model.sr)

wav = model.generate(
    "मुझे लगता है कि यह एक बहुत अच्छा विचार है क्योंकि हम इस प्रोजेक्ट का परीक्षण कर रहे हैं ताकि पता चले कि आवाज़ की नकल कितनी अच्छी तरह काम करती है",
    language_id="hi",
    audio_prompt_path=ref_audio,
)
ta.save("results/chatterbox/output_hindi.wav", wav, model.sr)

print("done")

from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")

ref_audio = "results/reference_v2.wav"

tts.tts_to_file(
    text="This is a test of zero shot voice cloning using X T T S version 2 where we are evaluating how natural and clear the cloned voice sounds when speaking a longer sentence for the Echo project",
    speaker_wav=ref_audio,
    language="en",
    file_path="results/xtts-v2/output_en.wav",
)

tts.tts_to_file(
    text="Mujhe lagta hai ki this is a really good idea yaar kyunki hum log is project ko test kar rahe hain taaki pata chale ki voice cloning kitni acchi kaam karti hai",
    speaker_wav=ref_audio,
    language="en",
    file_path="results/xtts-v2/output_hinglish.wav",
)

tts.tts_to_file(
    text="मुझे लगता है कि यह एक बहुत अच्छा विचार है क्योंकि हम इस प्रोजेक्ट का परीक्षण कर रहे हैं ताकि पता चले कि आवाज़ की नकल कितनी अच्छी तरह काम करती है",
    speaker_wav=ref_audio,
    language="hi",
    file_path="results/xtts-v2/output_hindi.wav",
)

print("done")

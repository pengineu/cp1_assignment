from chatterbox.tts import ChatterboxTTS


model = ChatterboxTTS.from_pretrained(device="cuda")
wav = model.generate(
    text="Hello, this is a cloned voice.",
    audio_prompt_path="reference.wav",
    exaggeration=0.5,  # 감정 강도 조절
)
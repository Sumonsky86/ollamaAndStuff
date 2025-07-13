import os
import requests
from google.cloud import texttospeech

# Query Ollama running on host (host.docker.internal works on Mac/Windows, use --network=host on Linux)
ollama_url = "http://host.docker.internal:11434/api/generate"
response = requests.post(ollama_url, json={
    "model": "mistral",
    "prompt": "What is the capital of France?"
})
print("Mistral response:", response.json().get("response"))

# Google TTS setup
client = texttospeech.TextToSpeechClient()
synthesis_input = texttospeech.SynthesisInput(text="Hello from Docker!")
voice = texttospeech.VoiceSelectionParams(language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
print("Google TTS audio saved as output.mp3")

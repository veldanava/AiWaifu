import openai
from gtts import gTTS
import os
import io
from pydub import AudioSegment
from pydub.playback import play

# This project was inspired by Adi Panda's YouTube channel content with the same topic namely AI Waifu, but this project is simpler

# ur openai key
openai.api_key = "paste in here"

print("Hello oniisan....")

# def function input
def chat():
    # Get user input
    input_text = input("question: ")

    # send query to ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        temperature=0.5,
        max_tokens=300,
        n=1,
        stop=None,
        timeout=20,
        )

    # get ChatGPT response
    output_text = response.choices[0].text.strip()

    # convert to speech using gTTS
    tts = gTTS(text=output_text, lang='ja')

    # play the speech using PyDub
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    audio_data = AudioSegment.from_file(audio_bytes, format="mp3")

    play(audio_data)

# run with loop
while True:
    chat()

import speech_recognition as sr
from pydub import AudioSegment
import os

filename = "Recording(23).wav"

r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)
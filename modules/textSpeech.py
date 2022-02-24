import gtts
from playsound import playsound

tts = gtts.gTTS("Hello World!")
tts.save("send.mp3")
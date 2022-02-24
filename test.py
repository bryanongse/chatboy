import pyttsx3
engine = pyttsx3.init()
# convert this text to speech
text = "Python is a great programming language"
engine.setProperty("rate", 150)
engine.say(text)
# play the speech
engine.runAndWait()
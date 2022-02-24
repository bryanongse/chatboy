from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import speech_recognition as sr
import gtts
from playsound import playsound

##### Pred Emotions Var
model_name= "bhadresh-savani/distilbert-base-uncased-emotion"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer, return_all_scores = True)

##### Speech to Text Var
r = sr.Recognizer()


def predEmotions(text):
    return classifier(text)

def speechToText(filename):
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text

def textToSpeech(text):
    tts = gtts.gTTS(text)
    tts.save("send.mp3")
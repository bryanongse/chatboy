from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import speech_recognition as sr
import gtts
from playsound import playsound
import random
import sounddevice as sd
from scipy.io.wavfile import write
from io import BytesIO
import time



##### Pred Emotions Var
model_name= "bhadresh-savani/distilbert-base-uncased-emotion"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer, return_all_scores = True)

##### Speech to Text Var
r = sr.Recognizer()

##### Recording Var
freq = 44100
duration = 5

##### Global Variables
flag = 0
score = 0
scenerioNo = 2
threshold = 1.9
continueNo = 7
successNo = 4
filename = "recording0.wav"

def predEmotions(text):
    return classifier(text)

def speechToText(filename):
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text

def textToSpeech(text):
    mp3_fp = BytesIO()
    tts = gtts.gTTS(text)
    num = random.randint(0,1000)
    name = "send" + str(num) +".mp3"
    tts.save("./sound/"+name)
    time.sleep(0.5)
    playsound("./sound/"+name)


def scoreCalc(results):
    # can do more advanced stuff as well

    score = 0
    results = results[0] # retrive the list of dictionaries
    # sadness joy love anger fear surprise
    for class_ in results:
        if class_['label'] == "joy" or class_['label'] == "love":
            score += class_['score']
        else:
            score -= class_['score']

def record():
    recording = sd.rec(int(duration * freq),
                       samplerate=freq, channels=2)
    sd.wait()

    num = random.randint(0, 1000)
    name = "recording" + str(num) + ".wav"
    write("./song"+name, freq, recording)

    text = speechToText("./song"+name)  # filename is the directory where the user's file is downloaded ###########################

    return text

def Scenerio():
    score =0
    while score < threshold:
        lst = [flag, score]

        if lst[0] == 0: # means flag is not raised; first iteration
            lst[0] = 1
            # scenerio to text
            with open('scenerio.txt') as f:
                scen = f.read().splitlines()
                noOfLines = int(scen[0])
                for n in range(noOfLines):
                    textToSpeech(scen[1+n])
            # wait for response #####################
            text = record()
            # change score accordingly
            results = predEmotions(text)
            score = scoreCalc(results)

            if score > threshold:
                # play success
                with open('success.txt') as f:
                    scs = f.read().splitlines()
                    choiceS = random.randint(0, successNo - 1)
                    textToSpeech(scs[choiceS])
                    break
            else:
                continue
        else: ###### means in the middle ######
            with open('continue.txt') as f:
                ctn = f.read().splitlines()
                choice = random.randint(0,continueNo-1)
                textToSpeech(ctn[choice])
            # wait for response
            text = speechToText(filename)  # filename is the directory where the user's file is downloaded ###########################
            # change score accordingly
            results = predEmotions(text)
            score = scoreCalc(results)

            if score > threshold:
                # play success
                with open('success.txt') as f:
                    scs = f.read().splitlines()
                    choiceS = random.randint(0, successNo - 1)
                    textToSpeech(scs[choiceS])
                    break
            else:
                continue


Scenerio()
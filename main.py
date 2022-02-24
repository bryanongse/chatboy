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
import wavio
from detoxify import Detoxify
import pyttsx3


##### Pred Emotions Var
model_name= "bhadresh-savani/distilbert-base-uncased-emotion"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer, return_all_scores = True)

##### Speech to Text Var
r = sr.Recognizer()
engine = pyttsx3.init()

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

def predEmotions(text):
    res = classifier(text)
    #res2 = Detoxify('original').predict(text)
    res2 = {'toxicity': 0} ################################################## CHANGE THIS!!!!!!!
    result = [res,res2]
    return result

def speechToText(filename):
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text

def textToSpeech(text, flag):
    if flag == 1:
        engine.setProperty("rate", 150)
        engine.say(text)
        # play the speech
        engine.runAndWait()
    else:
        mp3_fp = BytesIO()
        tts = gtts.gTTS(text)
        num = random.randint(0,1000)
        name = "send" + str(num) +".mp3"
        tts.save("./sound/"+name)
        time.sleep(0.5)
        playsound("./sound/"+name)


def scoreCalc(results):
    # can do more advanced stuff as well
    res1 = results[1]
    res2 = results[0]
    score = 0
    res2 = res2[0] # retrive the list of dictionaries
    # sadness joy love anger fear surprise
    for class_ in res2:
        if class_['label'] == "joy" or class_['label'] == "love":
            score += (class_['score'] * 1.25)
        else:
            score -= (class_['score'] * 0.25)
    score *= (1-res1['toxicity'])
    print(score)
    return score

def record():
    #playsound("ding.mp3")

    recording = sd.rec(int(duration * freq),
                       samplerate=freq, channels=2)
    sd.wait()

    num = random.randint(0, 1000)
    name = "recording" + str(num) + ".wav"
    wavio.write("./sound/"+name, recording, freq, sampwidth=2)

    text = speechToText("./sound/"+name)  # filename is the directory where the user's file is downloaded ###########################

    return text

def Scenerio():

    ##### Global Variables
    flag = 0
    score = 0
    scenerioNo = 2
    threshold = 2.5
    continueNo = 7
    successNo = 4

    lst = [flag, score]

    while score < threshold:

        if lst[0] == 0: # means flag is not raised; first iteration
            lst[0] = 1
            # scenerio to text
            with open('scenerio.txt') as f:
                scen = f.read().splitlines()
                noOfLines = int(scen[0])
                for n in range(noOfLines):
                    textToSpeech(scen[1+n], abs(n%2-1))
            # wait for response #####################
            text = record()
            # change score accordingly
            results = predEmotions(text)
            score += scoreCalc(results)

            if score > threshold:
                playsound("success.wav")
                # play success
                with open('success.txt') as f:
                    scs = f.read().splitlines()
                    choiceS = random.randint(0, successNo - 1)
                    textToSpeech(scs[choiceS], 0)
                    break
            else:
                continue
        else: ###### means in the middle ######
            with open('continue.txt') as f:
                ctn = f.read().splitlines()
                choice = random.randint(0,continueNo-1)
                textToSpeech(ctn[choice], 0)
            # wait for response
            text = record()
            # change score accordingly
            results = predEmotions(text)
            score += scoreCalc(results)

            if score > threshold:
                # play success
                playsound("success.wav")
                with open('success.txt') as f:
                    scs = f.read().splitlines()
                    choiceS = random.randint(0, successNo - 1)
                    textToSpeech(scs[choiceS], 0)
                    break
            else:
                continue


Scenerio()
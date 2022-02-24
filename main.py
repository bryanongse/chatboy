from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name= "bhadresh-savani/distilbert-base-uncased-emotion"

model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer)

def predEmotions(text):
    return classifier(text)

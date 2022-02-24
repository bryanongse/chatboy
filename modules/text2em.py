from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

import torch
import torch.nn.functional as F

model_name= "bhadresh-savani/distilbert-base-uncased-emotion"

model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer, return_all_scores = True)
res = classifier("Syrup can you come down sir can you come down at this point in time served can you calm down")

print(res)

# tokens = tokenizer.tokenize("Sir please calm down")
# token_ids = tokenizer.convert_tokens_to_ids(tokens)
#
# print(tokens)
# print(token_ids)
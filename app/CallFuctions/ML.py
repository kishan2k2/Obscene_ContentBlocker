from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from transformers import pipeline
model_nlp = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
sentiment_task = pipeline("sentiment-analysis", model=model_nlp, tokenizer=tokenizer)
def huggingface(data):
    # return data
    positive = 0; negitive = 0; neutral = 0
    for i in range(0, len(data), 10):
        temp = data[i:i+10]
        sentence = ""
        for i in temp:
            sentence += i + " "
        label=sentiment_task(sentence)[0]['label']
        # print(type(label))
        if label=='positive':
            positive += 1
        elif label=='negative':
            negitive += 1
        else:
            neutral += 1
        print(sentence)#Remove this statement after checking for a bit.
    ratio = (negitive/(neutral+positive))*100
    if ratio >= 5:
        result = True
    else:
        result = False
    return {
        "result": result
    }
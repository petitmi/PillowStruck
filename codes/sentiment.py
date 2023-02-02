import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from lyrics import Lyrics

class Sentiment():
    def __init__(self):
        self.model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
  
    def sentiment_analysis_on_lyrics(self,qs=['space%20oddity%20david%20bowie']):
        getLyrics = Lyrics()
        filenames = getLyrics.get_lyrics(qs)
        scores = []
        filename = filenames[0]
        with open(filename) as f:
            raw_data = f.read().splitlines()
            raw_data = [i for i in raw_data if i != '']
        classifier = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)
        rsts = classifier(raw_data)
        score = pd.DataFrame()
        for rst_index in range(len(rsts)):
            if rsts[rst_index]['label']=='positive':
                score_nl = pd.DataFrame(data={'line':[raw_data[rst_index]],'score':[rsts[rst_index]['score']]})
            elif rsts[rst_index]['label']=='negative':
                score_nl = pd.DataFrame(data={'line':[raw_data[rst_index]],'score':[-rsts[rst_index]['score']]})
            else :
                score_nl = pd.DataFrame(data={'line':[raw_data[rst_index]],'score':[0]})
            score = pd.concat([score, score_nl], ignore_index=True)
        scores.append(score)
        return scores
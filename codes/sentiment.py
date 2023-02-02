import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from lyrics import Lyrics

class Sentiment(Lyrics):
    def __init__(self,qs):
        Lyrics.__init__(self, qs)
        self.model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
  
    def sentiment_analysis_on_lyrics(self,filename):
        filenames = Lyrics.get_lyrics()
        filename = filenames[0]
        with open(filename) as f:
            raw_data = f.read().splitlines()
            raw_data = [i for i in raw_data if i != '']
        classifier = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)
        rsts = classifier(raw_data)
        scores = pd.DataFrame()
        for rst_index in range(len(rsts)):
            if rsts[rst_index]['label']=='positive':
                score_nl = pd.DataFrame(data={'line':[raw_data[rst_index]],'score':[rsts[rst_index]['score']]})
            elif rsts[rst_index]['label']=='negative':
                score_nl = pd.DataFrame(data={'line':[raw_data[rst_index]],'score':[-rsts[rst_index]['score']]})
            else :
                score_nl = pd.DataFrame(data={'line':[raw_data[rst_index]],'score':[0]})
            scores = pd.concat([scores, score_nl], ignore_index=True)
        return scores
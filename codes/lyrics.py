import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

class Lyrics:
    def __init__(self):
        self.headers={
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        #for craw
        self.ss = requests.Session()
        #for sentiment analysis
        self.model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    def get_lyrics(self,q=[['David-Bowie','Space-Oddity']]):
        for pairs in q:
            req = self.ss.get(
              f'https://www.musixmatch.com/lyrics/{pairs[0]}/{pairs[1]}', 
              headers=self.headers
            )
            soup = BeautifulSoup(req.text, features="lxml")
            spans = soup.find_all('span', attrs={'class':'lyrics__content__ok'})
            for span in spans:
                print(span.string)
            time.sleep(random.uniform(0.8, 0.2))
    def sentiment_analysis_on_lyrics(self,q):
      a = Lyrics()
      a.get_lyrics(q)
      
      with open(f'{q[0][0]}_{q[0][1]}.txt') as f:
          raw_data = f.read().splitlines()
          raw_data = [i for i in raw_data if i != '']
      classifier = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)
      rsts = classifier(raw_data)
      print(rsts)
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
            
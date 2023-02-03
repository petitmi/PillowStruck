import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from lyrics_rub import LyricsRub
from wordcloud import WordCloud

import matplotlib.pyplot as plt

class LyricsStruck():
    def __init__(self,qs):
        self.model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        getLyrics = LyricsRub()
        self.filenames = getLyrics.get_lyrics(qs)

    def process_lyrics(self):
        """     
        lyrics_line_lst: [['',''],['','']]
        lyrics_str_lst: ['','']
        comp_lyrics_line_lst:['','']
        comp_lyrics_str: ''
        """
        lyrics_line_lst = []
        lyrics_str_lst=[]
        for filename in self.filenames:
            with open(filename) as f:
                raw_data = f.read().splitlines()
                raw_data = [i for i in raw_data if i != '']
                lyrics_line_lst.append(raw_data)
                lyrics_str_lst.append('. '.join(raw_data))
        comp_lyrics_str = '. '.join(lyrics_str_lst)
        comp_lyrics_line_lst = [item for sublist in lyrics_line_lst for item in sublist]

        return comp_lyrics_str, comp_lyrics_line_lst, lyrics_str_lst, lyrics_line_lst

    def word_cloud(self):
        comp_lyrics_str,_,_,_ = self.process_lyrics()

        fig, ax = plt.subplots()
        wordcloud = WordCloud(
            background_color='black', max_words=200, max_font_size=40, scale=1, random_state=1
            ).generate(comp_lyrics_str)
        ax.imshow(wordcloud)
        ax.axis('off')
        ax.set_title('&'.join(self.filenames[7:-4]))
        
        plt.show()
        # plt.savefig(f"{self.filenames[idx+1]}.png")     

    def sentiment_analysis(self):
        comp_lyrics_str, comp_lyrics_line_lst, lyrics_str_lst, lyrics_line_lst = self.process_lyrics()

        # multiple tracks input
        comp_score = None
        scores = {}
            
        # use transformer do sentiment analysis
        for idx_file, lyrics in enumerate(lyrics_line_lst):
            classifier = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)
            rsts = classifier(lyrics)
            # compute and write scores
            line_score_df = pd.DataFrame()
            for idx_line, line_rst in enumerate(rsts):
                if line_rst['label']=='positive':
                    _line_score_df = pd.DataFrame(data={'line':[lyrics[idx_line]],'score':[line_rst['score']]})
                elif line_rst['label']=='negative':
                    _line_score_df = pd.DataFrame(data={'line':[lyrics[idx_line]],'score':[-line_rst['score']]})
                else :
                    _line_score_df = pd.DataFrame(data={'line':[lyrics[idx_line]],'score':[0]})
                
                line_score_df = pd.concat([line_score_df, _line_score_df], ignore_index=True)
            comp_track_score = sum(line_score_df['score'])/len(line_score_df['score'])
            scores[self.filenames[idx_file][7:-4]]=[comp_track_score, line_score_df]

        _comp_track_scores = [scores[s][0] for s in scores]
        comp_score = sum(_comp_track_scores)/len(_comp_track_scores)

        return comp_score, scores

from lyrics_rub import LyricsRub
import os
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

class LyricsStruck():
    def __init__(self,q='space%20oddity%20david%20bowie'):
        getLyrics = LyricsRub()
        self.filename, self.lyrics_str, self.lyrics_line_lst = getLyrics.process_lyrics(q)
        logging.info('------------',self.filename,'----------',self.lyrics_str, '---------------',self.lyrics_line_lst)

        

    def word_cloud(self):
        from wordcloud import WordCloud

        wordcloud_pic = f"wordcloud_{self.lyrics_line_lst[0][0]}.png"
        if not os.path.exists(f'static/{wordcloud_pic}'):
            wordcloud = WordCloud(
                background_color='white', colormap='hot',max_words=1200, max_font_size=100, scale=1, random_state=1,width=1600,height=300
                ).generate(self.lyrics_str)
            f'static/{wordcloud_pic}'
            wordcloud.to_file(f'static/{wordcloud_pic}')     

        return wordcloud_pic

        
            

    # def analyze_sentiment(self):
    #     import tweetnlp
    #     import pandas as pd

    #     # multiple tracks input
    #     model = tweetnlp.load_model('sentiment')  # Or `model = tweetnlp.Sentiment()` 

    #     comp_score, track_score, line_track_score = None, {}, {}
    #     # use transformer do sentiment analysis
    #     for idx_file, lyrics_line in enumerate(self.lyrics_line_lst):
    #         rsts = model.sentiment(lyrics_line, return_probability=True)
    #         # compute and write scores

    #         line_score_df = pd.DataFrame(data={'line':lyrics_line,'label':rsts['label'],'score':[rsts['probability'][rsts['label']]]})
    #     line_track_score[self.filename[7:-4]] = line_score_df
        
    #     _track_score =model.sentiment(self.lyrics_str, return_probability=True)
    #     track_score[self.filename[7:-4]] = {'label':_track_score['label'],'score':_track_score['probability'][_track_score['label']]}

    #     return track_score, line_track_score
    
    # def visualize_sentiment(self):
    #     import altair as alt
    #     alt.renderers.enable('altair_saver', fmts=['vega-lite', 'png'])

    #     comp_score, track_score, line_track_score = self.analyze_sentiment()
    #     df = line_track_score['David-Bowie_Space-Oddity-Solo-Home-Demo-Fragment'].reset_index()
    #     df['score']=df['score'].round(2)
    #     source = df.loc[1:,]
    #     #set colors
    #     color_scale = alt.Scale(
    #         domain=["positive","neutral","negative"],range=["#FF5F1F", "#008000", "#483D8B"]
    #     )
    #     chart_title = alt.TitleParams(
    #     'Lyric Lines Sentiment Analysis',    
    #     subtitle = df.loc[:0,]['line'].values[0]
    #     )
    #     #make bar plot
    #     bars = alt.Chart(source,title=chart_title).mark_bar().encode(
    #         x=alt.X('mean(score):Q'),
    #         y=alt.Y('line:N', sort=None),
    #         color = alt.Color('label:N',title = 'Sentiment label', scale=color_scale,),
    #         opacity=alt.Opacity('mean(score):Q')
    #     )
    #     # add tezt
    #     text = bars.mark_text(color='white',align='left',dx=3).encode(
    #         text='mean(score):Q'
    #     )

    #     chart = bars + text
    #     chart.properties(height=600).configure_axisY(
    #         titleAngle=0, titleY=-10,titleX=-60,labelPadding=160, labelAlign='left'
    #     )
        
    #     chart.save(f"{df.iloc[0,0]}.png")
        
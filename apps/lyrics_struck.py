from lyrics_rub import LyricsRub
import os
import logging
import pandas as pd
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

class LyricsStruck():
    def __init__(self,filename):
        getLyrics = LyricsRub()
        self.filename = filename
        self.lyrics_str, self.lyrics_line_lst = getLyrics.process_lyrics(filename)
        logging.info('------------',filename,'----------',self.lyrics_str, '---------------',self.lyrics_line_lst)


    def word_cloud(self):
        from wordcloud import WordCloud

        wordcloud_pic = f"wordcloud_{self.lyrics_line_lst[0]}.png"
        if not os.path.exists(f'static/tracks/{wordcloud_pic}'):
            wordcloud = WordCloud(
                background_color='white', colormap='hot',max_words=1200, max_font_size=100, scale=1, random_state=1,width=1600,height=300
                ).generate(self.lyrics_str)
            wordcloud.to_file(f'static/tracks/{wordcloud_pic}')     
        return wordcloud_pic


    def analyze_sentiment(self):
        import tweetnlp
        import pandas as pd

        # multiple tracks input
        model = tweetnlp.load_model('sentiment')  # Or `model = tweetnlp.Sentiment()` 
        score_line_df = pd.DataFrame()
        line_score_lst = model.sentiment(self.lyrics_line_lst, return_probability=True)
        # use transformer do sentiment analysis
        for idx_file, lyrics_line in enumerate(line_score_lst):
            # compute and write scores
            score_line_df = pd.concat([score_line_df, pd.DataFrame(
                data={'line':[self.lyrics_line_lst[idx_file]],
                    'label':[lyrics_line['label']],
                    'score':[lyrics_line['probability'][lyrics_line['label']]]
                    }
                )]
            )  
        _score_track =model.sentiment(self.lyrics_str, return_probability=True)
        score_track = {'label':_score_track['label'],
        'score':_score_track['probability'][_score_track['label']]}
        return score_track, score_line_df
    
    def visualize_sentiment(self):
        import altair as alt
        # alt.renderers.enable('altair_saver', fmts=['vega-lite', 'png'])

        track_score, score_line_df = self.analyze_sentiment()
        df = score_line_df.reset_index()
        df['score']=df['score'].round(2)
        source = df.loc[1:,]
        #set colors
        color_scale = alt.Scale(
            domain=["positive","neutral","negative"],range=["#FF5F1F", "#008000", "#483D8B"]
        )
        chart_title = alt.TitleParams(
        'Lyric Lines Sentiment Analysis',    
        subtitle = df.loc[:0,]['line'].values[0]
        )
        #make bar plot
        bars = alt.Chart(source,title=chart_title).mark_bar().encode(
            x=alt.X('mean(score):Q'),
            y=alt.Y('line:N', sort=None),
            color = alt.Color('label:N',title = 'Sentiment label', scale=color_scale,),
            opacity=alt.Opacity('mean(score):Q')
        )
        # add tezt
        text = bars.mark_text(color='white',align='left',dx=3).encode(
            text='mean(score):Q'
        )

        chart = bars + text
        chart.properties(height=600).configure_axisY(
            titleAngle=0, titleY=-10,titleX=-60,labelPadding=160, labelAlign='left'
        )
        return chart
        
        # chart.save('chart.png')
        
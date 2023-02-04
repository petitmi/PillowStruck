import pandas as pd
from lyrics_rub import LyricsRub
from wordcloud import WordCloud
import tweetnlp
import matplotlib.pyplot as plt
import altair as alt
from altair_saver import save


class LyricsStruck():
    def __init__(self,qs=['space%20oddity%20david%20bowie']):
        getLyrics = LyricsRub()
        self.filenames, self.comp_lyrics_str, self.comp_lyrics_line_lst, self.lyrics_str_lst, self.lyrics_line_lst = getLyrics.process_lyrics(qs)
        alt.renderers.enable('altair_saver', fmts=['vega-lite', 'png'])

    def word_cloud(self):
        fig, ax = plt.subplots()
        wordcloud = WordCloud(
            background_color='black', max_words=200, max_font_size=40, scale=1, random_state=1
            ).generate(self.comp_lyrics_str)
        ax.imshow(wordcloud)
        ax.axis('off')
        ax.set_title('&'.join(self.filenames[7:-4]))
        plt.show()
        # plt.savefig(f"{self.filenames[idx+1]}.png")     

    def analyze_sentiment(self):
        # multiple tracks input
        model = tweetnlp.load_model('sentiment')  # Or `model = tweetnlp.Sentiment()` 

        comp_score, track_score, line_track_score = None, {}, {}
        # use transformer do sentiment analysis
        for idx_file, lyrics_line in enumerate(self.lyrics_line_lst):
            rsts = model.sentiment(lyrics_line, return_probability=True)
            # compute and write scores
            # line_score
            line_score_df = pd.DataFrame()
            for idx_line, line_rst in enumerate(rsts):
                _line_score_df = pd.DataFrame(data={'line':[lyrics_line[idx_line]],'label':line_rst['label'],'score':[line_rst['probability'][line_rst['label']]]})
                line_score_df = pd.concat([line_score_df, _line_score_df], ignore_index=True)
            line_track_score[self.filenames[idx_file][7:-4]] = line_score_df
            # track_score
            _track_score =model.sentiment(self.lyrics_str_lst[idx_file], return_probability=True)
            track_score[self.filenames[idx_file][7:-4]] = {'label':_track_score['label'],'score':_track_score['probability'][_track_score['label']]}
        #compact score
        _comp_score = model.sentiment(self.comp_lyrics_str, return_probability=True)
        comp_score = {'label':_comp_score['label'],'score':_comp_score['probability'][_comp_score['label']]}
        return comp_score, track_score, line_track_score
    
    def visualize_sentiment(self):

        comp_score, track_score, line_track_score = self.analyze_sentiment()
        df = line_track_score['David-Bowie_Space-Oddity-Solo-Home-Demo-Fragment'].reset_index()
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
        
        chart.save(f"{df.iloc[0,0]}.png")
        
from flask import Flask,render_template, request, redirect, url_for, session
import urllib.parse
from spotify_stare import *
from lyrics_rub import *
import pandas as pd
from lyrics_struck import *
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.secret_key = 'shit123kjnsdf(()*3kj'
    l = SpotifyStare()

    # Simple route
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/search')
    def search():
        if request.method == 'POST':
            session['keyword'] = request.form['keyword']
            session['keyword_encode'] = urllib.parse.quote(request.form['keyword'])
            return redirect('/result')
        else:
            return render_template('search.html')

    @app.route('/result')
    def result():
        keyword=session['keyword']
        artists, albums, tracks = l.search(q=session['keyword_encode'])

        return render_template(
            'result.html',
            keyword = keyword,
            artists = artists.loc[:5,['artist','followers','genres','explore']].to_html(escape=False),
            albums = albums.loc[:5,['album','release_date','artist','total_tracks','explore']].to_html(escape=False),
            tracks = tracks.loc[:10,['track','release_date','popularity','artist','album','explore']].to_html(escape=False)
        )
        
    @app.route('/track/<artist>_<track>')
    def track(track=None,artist=None):
        q=f'{track}%20{artist}'
        logging.info(q)
        try:
            ls=LyricsStruck(q)
            lyrics_line_lst = ls.lyrics_line_lst
            lyrics = pd.DataFrame(lyrics_line_lst[1:],columns=[lyrics_line_lst[0]])
            lyrics = lyrics.to_html()
            wordcloud_pic = ls.word_cloud()
        except Exception as ex:
            logging.warning(ex)
            lyrics=None
            wordcloud_pic=''

        return render_template(
            'track.html',
            track =track,artist=artist,
            lyrics = lyrics,
            wordcloud_pic=wordcloud_pic
        )
        
    return app 


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0',port=8080,debug=True)


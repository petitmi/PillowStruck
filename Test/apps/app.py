from flask import Flask,render_template, request, redirect, url_for, session
from flask_caching import Cache

import urllib.parse
from spotify_stare import *
from lyrics_rub import *
import pandas as pd
from lyrics_struck import *
from artist_struck import *
import logging

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(config)
    cache = Cache(app)
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
            artists = artists.loc[:3,['artist','followers','genres','explore']].to_html(escape=False),
            albums = albums.loc[:5,['album','release_date','artist','total_tracks','explore']].to_html(escape=False),
            tracks = tracks.loc[:7,['track','release_date','popularity','artist','album','explore']].to_html(escape=False)
        )
        
    @app.route('/track/<artist>_<track>')
    def track(track=None,artist=None):
        q=f'{track}%20{artist}'
        try:
            # get lyrics file
            lr=LyricsRub()
            filename = lr.get_lyrics(q)
            ls=LyricsStruck(filename)
            if ls is not None :
                lyrics_line_lst = ls.lyrics_line_lst
                lyrics_pic = lyrics_line_lst[0]
                lyrics = pd.DataFrame(lyrics_line_lst[1:],columns=[lyrics_line_lst[0]])
                if len(lyrics)==0:
                    lyrics_sig = 1
                else: lyrics_sig = 0
                lyrics = lyrics.to_html()
                wordcloud_pic = ls.word_cloud()
            else:
                lyrics = None
                lyrics_pic = None
                wordcloud_pic = None
                lyrics_sig = 1                
            
        except Exception as ex:
            logging.warning(ex)

        return render_template(
            'track.html',
            track =track,artist=artist,
            lyrics = lyrics,
            wordcloud_pic=wordcloud_pic,
            lyrics_pic=lyrics_pic,
            lyrics_sig=lyrics_sig
        )

    @app.route('/artist/<artist>')
    @cache.cached(timeout=50)
    def artist(artist=None):
        try:
            ats = ArtistStruck()
            at_name = ats.get_artist_track_numbers_for_years(artist)
            pop_tracks = ats.get_artist_top_tracks_by_name(artist)
            pop_albums = ats.get_artist_albums_by_name(artist)
        except Exception as ex:
            logging.warning(ex)
            at_name,pop_tracks,pop_albums= None, None, None

        return render_template(
            'artist.html',artist=artist, artist_pic = f'{at_name}.png',
            pop_albums=pop_albums.to_html(),pop_tracks=pop_tracks.to_html()
        )

    @app.route('/songs-with-lyrics')
    def songlist():
        return render_template('songs-with-lyrics.html')
    
    return app 


if __name__ == "__main__":
    app = create_app()
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.run(host='0.0.0.0',port=8080,debug=True)


from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pandas as pd
from spotify_stare import *
import matplotlib
matplotlib.use('Agg')


class ArtistStruck:
    def __init__(self):
        sp = SpotifyStare()
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id=sp.client_id,
            client_secret=sp.client_secret
        ))

    def get_artist_id_by_name(self,name):
        results = self.sp.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            return items[0]['id']
        else:
            return None

    def get_album_id_by_name(self,name):
        results = self.sp.search(q='album:' + name, type='album')
        items = results['albums']['items']
        if len(items) > 0:
            return items[0]['id']
        else:
            return None
        
    def get_artist_info_by_name(self,name):
        results=self.sp.artist(self.get_artist_id_by_name(name))
        key=['name','genres','followers','popularity']
        value=[results['name'],results['genres'],results['followers']['total'],results['popularity']]
        my_dict={'info':key,'detail':value}
        return pd.DataFrame.from_dict(my_dict)
        
    def get_album_tracks_by_name(self,name):
        results=self.sp.album(self.get_album_id_by_name(name))
        tracks=results['tracks']['items']
        print("The number of tracks in this album is:",results['total_tracks'])
        print("track list:")
        i=1
        for track in tracks:
            print("%s. %s"%(i,track['name']))
            i=i+1

    def get_artist_albums_by_name(self,name,limit=10):
        results=self.sp.artist_albums(self.get_artist_id_by_name(name))
        albums=results['items']
        while results['next']:
            results = self.sp.next(results)
            albums.extend(results['items'])
        name_lst=[]
        release_date=[]
        tracks_num=[]
        for album in albums:
            name_lst.append(album['name'])
            release_date.append(album['release_date'])
            tracks_num.append(album['total_tracks'])
        album_dict={'Latest Album':name_lst,'Track Counts':tracks_num,'Release Date':release_date}
        my_data=pd.DataFrame.from_dict(album_dict)
        return my_data.drop_duplicates(subset=['Latest Album'],keep='first').sort_values(by='Release Date',ascending=False).head(limit)

    def get_artist_top_tracks_by_name(self,name):
        results=self.sp.artist_top_tracks(self.get_artist_id_by_name(name))
        tracks=results['tracks']
        name_lst=[]
        popularity=[]
        Album_name=[]
        date_lst=[]
        for item in tracks:
            name_lst.append(item['name'])
            popularity.append(item['popularity'])
            Album_name.append(item['album']['name'])
            date_lst.append(item['album']['release_date'])
        track_dict={'Top Track':name_lst,'Popularity':popularity,'Album':Album_name,'release date':date_lst}
        my_data=pd.DataFrame.from_dict(track_dict)
        return my_data.sort_values(by='Popularity',ascending=False)

    def get_artist_track_numbers_for_years(self,name):
        results=self.sp.artist_albums(self.get_artist_id_by_name(name))
        albums=results['items']
        while results['next']:
            results = self.sp.next(results)
            albums.extend(results['items'])
        name_lst=[]
        release_date=[]
        tracks_num=[]
        for album in albums:
            name_lst.append(album['name'])
            release_date.append(album['release_date'])
            tracks_num.append(album['total_tracks'])
        album_dict={'Album Name':name_lst,'Track Counts':tracks_num,'Release Date':release_date}
        my_data=pd.DataFrame.from_dict(album_dict)
        my_data=my_data.drop_duplicates(subset=['Album Name'],keep='first').sort_values(by='Release Date',ascending=False)
        my_data['Release Date']=pd.to_datetime(my_data['Release Date'])
        my_data=my_data.resample('Y',on='Release Date').sum().reset_index()
        my_data['Release Date']=my_data['Release Date'].dt.year
        fig = my_data.plot(x='Release Date',y= 'Track Counts',kind='bar',figsize=(10, 4),fontsize=8)
        fig=fig.get_figure()
        fig.savefig(f'static/{name}.png')
        return name
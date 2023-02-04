import base64
import requests
import yaml
import json
import pandas as pd

class SpotifyStare():
    def __init__(self):
        # Set the token url and token type. The client_id and client_secret is in the config.yml file and gitignored.
        self.token_url = 'https://accounts.spotify.com/api/token'
        self.token_data = {'grant_type':'client_credentials'}
        with open('../config.yml', "r") as f:
            client = yaml.safe_load(f)
        self.client_id= client['client_id']
        self.client_secret= client['client_secret']

    def login(self):

        client_creds = f"{self.client_id}:{self.client_secret}"
        #client_credentials: Base 64 encoded string that contains the client ID and client secret key. The field has the format: Authorization: Basic <base64 encoded client_id:client_secret>
        client_creds_b64 = base64.b64encode(client_creds.encode())
        token_headers = {"Authorization":f'Basic {client_creds_b64.decode()}'} 
        # post request
        req = requests.post(self.token_url, data=self.token_data, headers=token_headers)
        resp_token = req.json()
        return resp_token

    def search(self, type='track,artist,album',q='the%201975'):
        resp_token= self.login()
        search_headers= {'Content-Type': 'application/json', 'Host': 'api.spotify.com', "Authorization": f"Bearer {resp_token['access_token']}"}
        req_search = requests.get(f'https://api.spotify.com/v1/search?type={type}&q={q}', headers=search_headers)
        req_search = json.loads(req_search.text.replace('\n',''))
        artists, albums, tracks =[], [], []
        for item in req_search['artists']['items']:
            artist={}
            artist['artist'] = item['name']
            artist['id'] = item['id']
            artist['followers'] = item['followers']['total']
            artist['genres'] = item['genres']
            artist['explore'] = f"""<a href="/artist/{artist['artist']}"> gooo </a>"""

            # artist['type'] = item['type']
            artists.append(artist)
        for item in req_search['albums']['items']:
            album = {}
            album['album'] = item['name']
            album['id'] = item['id']
            album['release_date'] = item['release_date']
            album['total_tracks'] = item['total_tracks']
            album['artist'] = item['artists'][0]['name']
            album['artist_id'] = item['artists'][0]['id']
            album['explore'] = f"""<a href="/album/{album['album']}"> gooo </a>"""
            # album['type'] = item['type']
            albums.append(album)
        for item in req_search['tracks']['items']:
            track = {}
            track['track'] = item['name']
            track['release_date'] = item['album']['release_date']
            track['popularity'] = item['popularity']
            track['id'] = item['id']
            track['artist'] = item['artists'][0]['name']
            track['artist_id'] = item['artists'][0]['id']
            track['album'] = item['album']['name']
            track['album_id'] = item['album']['id']
            track['type'] = item['type']
            track['explore'] = f"""<a href="/track/{track['artist']}_{track['track']}"> gooo </a>"""
        
            tracks.append(track)
        artists = pd.DataFrame(artists)
        albums = pd.DataFrame(albums)
        tracks = pd.DataFrame(tracks)
        return artists, albums, tracks


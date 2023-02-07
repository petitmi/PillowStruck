from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import unittest
import requests
from artist_struck import ArtistStruck
from spotify_stare import SpotifyStare


class Test_artist_struck(unittest.TestCase):
    artist_cls=ArtistStruck()
    joji_id='3MZsBdqDrRTJihTHQrO6Dq'
    Birdy_id='1WGjSVIw0TVfbp5KrOFiP0'
    @classmethod

    def test_artist_id(self):
        self.assertTrue(self.artist_cls.get_artist_id_by_name('joji'),self.joji_id)

    def test_album_id(self):
        self.assertTrue(self.artist_cls.get_album_id_by_name('Birdy'),self.joji_id)

    def test_artist_info(self):
        self.assertTrue(self.artist_cls.get_artist_info_by_name('joji')['detail'][0],'Joji')
        self.assertTrue(self.artist_cls.get_artist_info_by_name('joji')['detail'][1],['pop', 'viral pop'])

    def test_album_tracks(self):
        self.assertIsNone(self.artist_cls.get_album_tracks_by_name('joji'))

    def test_artist_top_tracks(self):
        self.assertTrue(self.artist_cls.get_artist_top_tracks_by_name('joji')['Top Track'][1],'Die For You')
        self.assertTrue(self.artist_cls.get_artist_top_tracks_by_name('joji')['Top Track'][2],'SLOW DANCING IN THE DARK')
        self.assertTrue(self.artist_cls.get_artist_top_tracks_by_name('joji')['Top Track'][3],'worldstar money (interlude)')
        self.assertTrue(self.artist_cls.get_artist_top_tracks_by_name('joji')['Top Track'][4],'Sanctuary')
        
    def test_artist_albums(self):
        self.assertTrue(self.artist_cls.get_artist_albums_by_name('joji')['Latest Album'][0],'SMITHEREENS')
        self.assertTrue(self.artist_cls.get_artist_albums_by_name('joji')['Latest Album'][29],'Seasick')

if __name__ == '__main__':
    unittest.main()

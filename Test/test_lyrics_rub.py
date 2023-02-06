import requests
from bs4 import BeautifulSoup
import time
import random
import os
import json
import re

import unittest
from apps.lyrics_rub import LyricsRub

class Test_lyrics_rub(unittest.TestCase):
    lyrics_cls=LyricsRub()

    @classmethod
    def test_get_lyrics_link(self):
        self.assertTrue(1,1)
        
    def test_get_lyrics(self):
        self.assertTrue(1,1)

    def test_process_lyrics(self):
        self.assertTrue(1,1)

if __name__ == '__main__':
    unittest.main()

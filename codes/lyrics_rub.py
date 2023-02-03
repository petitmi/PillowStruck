import requests
from bs4 import BeautifulSoup
import time
import random
import os

class LyricsRub:
    def __init__(self):
        self.headers={
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        #for crawling
        self.ss = requests.Session()

    def get_lyrics_link(self, qs):
        print(qs)
        paths = []
        for q in qs:
            print('link:', f'https://www.musixmatch.com/search/{q}')
            req = self.ss.get(f'https://www.musixmatch.com/search/{q}',headers=self.headers) 
            soup = BeautifulSoup(req.text, features="lxml")
            h2s = soup.find_all('h2',attrs={'class':'media-card-title'})
            path = h2s[1].find_all('a')[0]
            paths.append(path['href'])
            time.sleep(random.uniform(0.8, 0.2))
        return paths
            
    def get_lyrics(self, qs=['space%20oddity%20david%20bowie']):
        paths = self.get_lyrics_link(qs)
        filenames = []
        for path in paths:
            trackname = path.split('/')[2:]
            trackname = '_'.join(trackname)
            filename = f"lyrics/{trackname}.txt"
            filenames.append(filename)
            # if file exists, remove it 
            if os.path.exists(filename):
              os.remove(filename)
            # write lyrics title
            f = open(filename, "a")
            f.write(trackname+'\n')

            #get lyrics from musixmatch
            req = self.ss.get(
              f'https://www.musixmatch.com{path}', 
              headers=self.headers
            )

            soup = BeautifulSoup(req.text, features="lxml")
            spans = soup.find_all('span', attrs={'class':'lyrics__content__ok'})
            for span in spans:
                f.write(span.string)
            time.sleep(random.uniform(0.8, 0.2))
        f.close()
        return filenames


            
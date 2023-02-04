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

    def get_lyrics_link(self, q):
        '''Using web crawling to search and locate to track'''
        
        req = self.ss.get(f'https://www.musixmatch.com/search/{q}',headers=self.headers) 
        soup = BeautifulSoup(req.text, features="lxml")
        h2s = soup.find_all('h2',attrs={'class':'media-card-title'})
        path = h2s[1].find_all('a')[0]
        path = path['href']
        # print('=============',path)
        time.sleep(random.uniform(0.8, 0.2))
        return path
            
    def get_lyrics(self, q):
        '''Using web crawling to get the lyrics of the destinated track'''
        path = self.get_lyrics_link(q)
    
        trackname = path.split('/')[2:]
        trackname = '_'.join(trackname)
        filename = f"lyrics/{trackname}.txt"
        # if file does not exist:
        if not os.path.exists(filename):
        #   os.remove(filename)
            # write lyrics title
            f = open(filename, "w")
            f.write(trackname+'\n')

            #get lyrics from musixmatch
            req = self.ss.get(f'https://www.musixmatch.com{path}', headers=self.headers
            )
            print('=============',req.text)
            soup = BeautifulSoup(req.text, features="lxml")
            spans = soup.find_all('span', attrs={'class':'lyrics__content__ok'})
            for span in spans:
                f.write(span.string)
            time.sleep(random.uniform(0.8, 0.2))
            f.close()
        return filename

    def process_lyrics(self,q='space%20oddity%20david%20bowie'):
        """ 
        Processing lyrics and get those objects:
        filenames: ['', '']    
        lyrics_line_lst: [['',''],['','']]
        lyrics_str_lst: ['','']
        comp_lyrics_line_lst:['','']
        comp_lyrics_str: ''
        """
        filename = self.get_lyrics(q)
        lyrics_line_lst = []
        print(',,,,,,,,,,,,,,,,,',filename)
        with open(filename) as f:
            lyrics_line_lst = f.read().splitlines()
            lyrics_line_lst = [i for i in lyrics_line_lst if i != '']
            lyrics_str='. '.join(lyrics_line_lst)

        return filename, lyrics_str, lyrics_line_lst

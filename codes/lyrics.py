import requests
from bs4 import BeautifulSoup

class Lyrics:
    def __init__(self):
        self.headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    def get_lyrics(self,artistName='David-Bowie',trackName='Space-Oddity'):
        req = requests.get(f'https://www.musixmatch.com/lyrics/{artistName}/{trackName}', headers=self.headers)
        soup = BeautifulSoup(req.text)
        spans = soup.find_all('span', attrs={'class':'lyrics__content__ok'})
        for span in spans:
            print(span.string)
            
from .login import *

class Searcher(Account):
    def __init__(self):
        Account.__init__(self)
    def search(self, type='track,artist',q='the%201975'):
        client = Account()
        resp_token= client.login()
        search_headers= {'Content-Type': 'application/json', 'Host': 'api.spotify.com', "Authorization": f"Bearer {resp_token['access_token']}"}
        req_search = requests.get(f'https://api.spotify.com/v1/search?type={type}&q={q}', headers=search_headers)
        return req_search
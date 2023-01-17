import base64
import requests
import yaml

class Account():
    def __init__(self):
        self.token_url = 'https://accounts.spotify.com/api/token'
        self.token_data = {'grant_type':'client_credentials'}
        with open('config.yml', "r") as f:
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

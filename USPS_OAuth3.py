import os
import requests


def get_token():
    data = '{"client_id":"", "client_secret":"", "grant_type":"client_credentials"}'

    headers = {
        'Content-Type': 'application/json'
    }

    url = 'https://api.usps.com/oauth2/v3/token'
    response = requests.post(url, data=data, headers=headers)
    print(response.text)



get_token()

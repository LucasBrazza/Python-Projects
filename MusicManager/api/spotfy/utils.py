# async def  getProfile(accessToken) {
#   let accessToken = localStorage.getItem('access_token');

#   const response = await fetch('https://api.spotify.com/v1/me', {
#     headers: {
#       Authorization: 'Bearer ' + accessToken
#     }
#   });

#   const data = await response.json();
# }

import requests
import os
from dotenv import load_dotenv


# Load environment variables from config.py
load_dotenv()


def getAccessToken():
    """
    Fetches an access token from the Spotify API using the client credentials flow.

    Returns:
    str or None: The access token if the request was successful, or None if the request failed.
    """
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': os.environ['SPOTFY_CLIENT_ID'],
        'client_secret': os.environ['SPOTFY_CLIENT_SECRET']
    }

    response = requests.post('https://accounts.spotify.com/api/token', headers = header, data = data)

    if response.status_code != 200:
        print(f'Error: Unable to fetch access token. Status code: {response.status_code}')
        return None

    os.environ['ACCESS_TOKEN'] = response.json()['access_token']
    return response.json()['access_token']



os.environ['ACCESS_TOKEN'] = getAccessToken()
print(os.environ['ACCESS_TOKEN'])

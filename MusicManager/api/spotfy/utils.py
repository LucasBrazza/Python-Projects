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
from flask import Flask, jsonify 


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
        'client_id': os.environ.get('SPOTFY_CLIENT_ID'),
        'client_secret': os.environ.get('SPOTFY_CLIENT_SECRET')
    }

    response = requests.post('https://accounts.spotify.com/api/token', headers = header, data = data)

    if response.status_code != 200:
        print(f'Error: Unable to fetch access token. Status code: {response.status_code}')
        return None

    os.environ['ACCESS_TOKEN'] = response.json()['access_token']
    return response.json()['access_token']

    



def getTrackById(accessToken, trackId):
    """
    Fetches track data from the Spotify API.

    Parameters:
    accessToken (str): The access token for the Spotify API.
    trackId (str): The ID of the track to fetch.

    Returns:
    dict or None: A dictionary containing the track data if the request was successful, or None if the request failed.
    """
    header = {
        'Authorization': f'Bearer {accessToken}'
    }

    response = requests.get(f'https://api.spotify.com/v1/tracks/{trackId}', headers = header)

    if response.status_code != 200:
        error_message = response.json().get("error").get("message") if response.json().get("error") else response.json()
        print(f'Error: Unable to fetch track data.\nStatus code: {response.status_code} - {error_message}')
        return None

    return response.json()

 
def getArtistById(accessToken, artistId):
    """
    Fetches artist data from the Spotify API.

    Parameters:
    accessToken (str): The access token for the Spotify API.
    artistId (str): The ID of the artist to fetch.
    
    Returns:
    dict or None: A dictionary containing the artist data if the request was successful, or None if the request failed.
    """
    
    header = {
        'Authorization': f'Bearer {accessToken}'
    }
    
    response = requests.get(f'https://api.spotify.com/v1/artists/{artistId}', headers = header)
    
    if response.status_code != 200:
        error_message = response.json().get("error").get("message") if response.json().get("error") else response.json()
        print(f'Error: Unable to fetch artist data.\nStatus code: {response.status_code} - {error_message}')
        return None
      
    return response.json()
 

def getProfile(accessToken) :
  
    header = {
        'Authorization': f'Bearer {accessToken}'
    }
    
    response = requests.get('https://api.spotify.com/v1/me', headers = header)
    
    if response.status_code != 200:
        error_message = response.json().get("error").get("message") if response.json().get("error") else response.json()
        print(f'Error: Unable to fetch user data.\nStatus code: {response.status_code} - {error_message}')
        return None
        
    return jsonify(response.json())


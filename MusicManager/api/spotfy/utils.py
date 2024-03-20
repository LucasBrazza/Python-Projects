import requests
import os
from dotenv import load_dotenv
from flask import Flask, jsonify , session, request, redirect
from datetime import datetime
import urllib.parse
import api.spotfy.security as security

# Load environment variables from config.py
load_dotenv()

def getAccessToken(grantType):
    
    if grantType == 'client_credentials':
        return getClientCredentialsToken()
    
    if grantType == 'authorization_code':
        return getAuthorizationCodeToken()


def getAuthorizationCodeToken():
    body = {
        'grant_type': 'authorization_code',
        'code': request.args['code'],
        'redirect_uri': os.environ.get('SPOTFY_REDIRECT_URI'),
        'client_id': os.environ.get('SPOTFY_CLIENT_ID'),
        'code_verifier': os.environ.get('CODE_VERIFIER')
    }

    response = requests.post(os.environ.get('TOKEN_URL'), data=body)

    tokeInfo = response.json()
    
    session['access_token'] = tokeInfo['access_token']
    session['refresh_token'] = tokeInfo['refresh_token']
    session['expires_at'] = datetime.now().timestamp() + tokeInfo['expires_in']

    if response.status_code != 200:
        print(f'Error: Unable to fetch access token. Status code: {response.status_code}')
        return None

    os.environ['ACCESS_TOKEN'] = response.json()['access_token']
    return response.json()['access_token']


def getClientCredentialsToken():
    """
    Fetches an access token from the Spotify API using the client credentials flow.

    Returns:
    str or None: The access token if the request was successful, or None if the request failed.
    """
    if session.get('access_token') != None and datetime.now().timestamp() > session['expires_at']:
        return refreshToken()
    
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
    session['access_token'] = response.json()['access_token']
    return response.json()['access_token']

    
def refreshToken():
    if 'refresh_token' not in session:
        return redirect('/login')
    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/login')
    
    body = {
        'grant_type' : 'refresh_token',
        'refresh_token' : session['refresh_token'],
        'client_id' : os.environ.get('SPOTFY_CLIENT_ID'),
        'client_secret' : os.environ.get('SPOTFY_CLIENT_SECRET')
    }
    
    response = requests.post(os.environ.get('TOKEN_URL'), data=body)
    newTokenInfo = response.json()
    
    session['access_token'] = newTokenInfo['access_token']
    session['expires_at'] = datetime.now().timestamp() + newTokenInfo['expires_in']


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


def getUserAuthorization():
    [codeVerified, codeChallenge] = security.AuthCodePKCEFlow()
    os.environ['CODE_VERIFIER'] = codeVerified
    os.environ['CODE_CHALLENGE'] = codeChallenge

    data = {
        'client_id': os.environ.get('SPOTFY_CLIENT_ID'),
        'response_type': 'code',
        'redirect_uri': os.environ.get('SPOTFY_REDIRECT_URI'),
        'code_challenge_method': 'S256',
        'code_challenge': codeChallenge,
        'scope': 'user-read-private user-read-email'
    }

    authUrl = f"{os.environ.get('AUTH_URL')}?{urllib.parse.urlencode(data)}"

    return redirect(authUrl)
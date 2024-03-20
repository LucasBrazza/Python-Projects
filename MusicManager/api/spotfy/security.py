import os
import urllib
import string
import secrets
import random
import hashlib
import base64
from flask import Flask, redirect
from dotenv import load_dotenv
# import flask object 'app' from app.py 

load_dotenv()

def AuthCodePKCEFlow(code=None):
    """
    Generates a code verifier and code challenge for the Spotify API.

    Returns:
    str: The code verifier.
    str: The code challenge.
    """
    if code is None:
        length = random.randint(43, 128)
        possible = string.ascii_letters + string.digits
        codeVerified = ''.join(secrets.choice(possible) for _ in range(length))
    else:
        codeVerified = code

    encoder = codeVerified.encode('utf-8')
    hashed = hashlib.sha256(encoder).digest()
    codeChallenge = base64.urlsafe_b64encode(hashed).rstrip(b'=').decode('utf-8')

    return codeVerified, codeChallenge

def decoder(codeVerifier: str) -> str:
    """
    Decodes the code verifier for the Spotify API.

    Parameters:
    codeVerifier (str): The code verifier to decode.

    Returns:
    str: The decoded code verifier.
    """
    return base64.urlsafe_b64encode(codeVerifier.encode('utf-8')).decode('utf-8')
    

def getUserAuthorization():
    [codeVerified, codeChallenge] = AuthCodePKCEFlow()
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
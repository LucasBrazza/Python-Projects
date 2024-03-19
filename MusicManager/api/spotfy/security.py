import os
import urllib
import string
import secrets
import random
import hashlib
import base64
from flask import Flask, redirect
from api.config import Config

app = Flask(__name__)
app.config.from_object(Config)


def AuthCodePKCEFlow(code=None) -> [str, str]: # type: ignore
    """
    Generates a code verifier for the Spotify API.

    Returns:
    str: The code verifier.
    """
    if code == None:
        length = random.randint(43, 128)
        possible = string.ascii_letters + string.digits 
        codeVerified = ''.join(secrets.choice(possible) for i in range(length))
    else:
        codeVerified = code
    
    encoder = codeVerified.encode('utf-8')
    hashed = hashlib.sha256(encoder).digest()

    return [codeVerified, hashed]

def decoder(codeVerifier: str) -> str:
    """
    Decodes the code verifier for the Spotify API.

    Parameters:
    codeVerifier (str): The code verifier to decode.

    Returns:
    str: The decoded code verifier.
    """
    return base64.urlsafe_b64encode(codeVerifier).decode('utf-8')
    

def getUserAuthorization():
    
    [codeVerified, hashed] = AuthCodePKCEFlow()
    app.config['CODE_VIRIFIER'] = codeVerified
    
    data = {
        'client_id': app.config['SPOTFY_CLIENT_ID'],
        'response_type': 'code',
        'redirect_uri': app.config['SPOTFY_REDIRECT_URI'],
        'code_challenge_method' : 'S256',
        'code_challenge' : hashed,
        'scope': 'user-read-private user-read-email'
    }
    
    authUrl = f"{app.config['AUTH_URL']}?{urllib.parse.urlencode(data)}"

    return redirect(authUrl)
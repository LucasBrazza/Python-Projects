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
    

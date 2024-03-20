import os
import api.spotfy.security as security
import api.spotfy.utils as spotfy
import api.config as config
from flask import Flask, request, redirect, session, jsonify
import requests
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return '<a href="/login">Login with Spotify</a>'


@app.route('/login')
def login():
    return security.getUserAuthorization()


@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"Error: ": request.args['error']})

    if 'code' in request.args:
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
        
        return redirect('/profile')
    

@app.route('/profile')
def profile():
    if 'access_token' not in session:
        return redirect('/login')
        
    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')
    
    return spotfy.getProfile(session['access_token'])


@app.route('/refresh-token')
def refreshToken():
    if 'refresh_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
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
        
        #TODO - return to the correct pages
        return redirect('/profile')
     
     
if __name__ ==  '__main__':
    app.run(host='0.0.0.0', port='8080' , debug=True)
import os
import api.spotfy.security as security
import api.spotfy.utils as spotfy
from api.config import Config
from flask import Flask, request, redirect, session, jsonify
import requests
from datetime import datetime
from dotenv import load_dotenv



app = Flask(__name__)
app.config.from_object(Config)


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
        request_body = {
            'code' : security.AuthCodePKCEFlow(request.args['code']),
            'grant_type' : 'authorization_code',
            'redirect_uri' : app.config['REDIRECT_URI'],
            'client_id' : app.config['SPOTFY_CLIENT_ID'],
            'client_secret' : app.config['SPOTFY_CLIENT_SECRET']
        }
        
        response = requests.post(app.config['TOKEN_URL'], data=request_body)
        
        print('\n\n---------------------------------')
        print(app.config['SPOTFY_CLIENT_ID'])
        print(app.config['SPOTFY_CLIENT_SECRET'])
        print(response.json())
        print('\n\n---------------------------------')
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
            'client_id' : app.config['SPOTFY_CLIENT_ID'],
            'client_secret' : app.config['SPOTFY_CLIENT_SECRET']
        }
        
        response = requests.post(app.config['TOKEN_URL'], data=body)
        newTokenInfo = response.json()
        
        session['access_token'] = newTokenInfo['access_token']
        session['expires_at'] = datetime.now().timestamp() + newTokenInfo['expires_in']
        
        #TODO - return to the correct pages
        return redirect('/profile')
     
     
if __name__ ==  '__main__':
    app.run(host='0.0.0.0', port='8080' , debug=True)
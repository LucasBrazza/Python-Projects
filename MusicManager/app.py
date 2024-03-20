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
    return spotfy.getUserAuthorization()


@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"Error: ": request.args['error']})

    if 'code' in request.args:
        spotfy.getAccessToken('authorization_code')
        
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
        spotfy.refreshToken()
        
        #TODO - return to the correct pages
        return redirect('/profile')
     
     
if __name__ ==  '__main__':
    app.run(host='0.0.0.0', port='8080' , debug=True)
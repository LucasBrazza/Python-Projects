# Description: Configuration file for the API
import os

# Spotify API
#TODO: change name to spotfy
os.environ['SPOTFY_CLIENT_ID'] = ""
os.environ['SPOTFY_CLIENT_SECRET'] = ""
os.environ['SPOTFY_REDIRECT_URI'] = "http://localhost:8080/callback"
os.environ['SECRET_KEY'] = ""
os.environ['AUTH_URL'] = "https://accounts.spotify.com/authorize"
os.environ['TOKEN_URL'] = "https://accounts.spotify.com/api/token"
os.environ['API_URL'] = "https://api.spotify.com/v1"
os.environ['REDIRECT_URI'] = "http://localhost:8080/callback"



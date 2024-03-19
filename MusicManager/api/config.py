# Description: Configuration file for the API


# Spotify API
class Config:
    SPOTFY_CLIENT_ID = ""
    SPOTFY_CLIENT_SECRET = ""
    SPOTFY_REDIRECT_URI = "http://localhost:8080/callback"
    SECRET_KEY = ""

    AUTH_URL = "https://accounts.spotify.com/authorize"
    TOKEN_URL = "https://accounts.spotify.com/api/token"
    API_URL = "https://api.spotify.com/v1"
    REDIRECT_URI = "http://localhost:8080/callback"



import os
import api.config as config
import api.spotfy.utils as spotfy



os.environ['ACCESS_TOKEN'] = spotfy.getAccessToken()
print(os.environ['ACCESS_TOKEN'])
artist = spotfy.getArtistById(os.environ['ACCESS_TOKEN'], "4Z8W4fKeB5YxbusRsdQVPb")
print(artist.get("name"))
profile = spotfy.getProfile(os.environ['ACCESS_TOKEN'])
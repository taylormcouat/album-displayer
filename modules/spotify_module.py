import spotipy
import os

class SpotifyModule:
    def __init__(self):
        client_id = 'a3d844a73c874bff8d09d05f65f622da'
        client_secret = '657480db2dab4f09a0fef0c4f318bfef'
        redirect_uri = 'https://127.0.0.1/callback'
        os.environ["SPOTIPY_CLIENT_ID"] = client_id
        os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret
        os.environ["SPOTIPY_REDIRECT_URI"] = redirect_uri
        scope = 'user-read-currently-playing'
        try:
            self.auth_manager = spotipy.SpotifyOAuth(scope=scope, open_browser=False)
            self.sp = spotipy.Spotify(auth_manager=self.auth_manager, requests_timeout=10)
        except Exception as e:
            print(e)
    
    def get_current_playing_song_art(self):
        try:
            track = self.sp.current_user_playing_track()
            if (track and track['item'] is not None):
                return track['item']['album']['images'][0]['url']
            else:
                return ""
        except Exception as e:
            print(e)
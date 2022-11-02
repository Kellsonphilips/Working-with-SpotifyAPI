import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("REDIRECT_URI")


def set_client():
    """
    - Authenticates spotify user using spotipy client
    - Set client scope for authentication
    :return: auth_manager, user_id, user_info
    """

    spotify = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            scope="playlist-modify-private playlist-read-private",
            cache_path="token.txt",
            show_dialog=True
        )
    )

    user_id = spotify.current_user()["id"]
    user_info = spotify.current_user()
    return spotify, user_id, user_info

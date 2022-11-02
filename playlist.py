import sys

from auth0 import set_client
from scrap import date, get_song

spotify, user_id, user_info = set_client()
title, song_names = get_song()
is_playlist_exist = False


def list_and_songs():
    """
    - Search for songs from Billboard music on Spotify
    - Find all songs uri
    - Create a list of songs from all songs and
    - Create a playlist on Spotify with the help of Authentication Manager
    - Add all songs to Spotify playlist with song Uri
    :return: error message in console if unsuccessfully or a song is not found
    """

    global is_playlist_exist
    song_uris = []
    year = date.split("-")[0]

    for song in song_names:
        res = spotify.search(q=f"track:{song} year:{year}", type="track", market="US")

        try:
            uri = res["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} not found in Spotify.")

    new_playlist_name = f"{date} {title}"
    all_playlist = spotify.current_user_playlists(limit=50, offset=0)
    playlist_names = all_playlist["items"]
    for playlist_ in playlist_names:
        if playlist_["name"] == new_playlist_name:
            is_playlist_exist = True
    if is_playlist_exist:
        sys.exit(f"This playlist '{new_playlist_name}' already exists.\nPlaylist not created.")
    elif not is_playlist_exist:
        playlist = spotify.user_playlist_create(user=user_id,
                                                name=new_playlist_name,
                                                description=f"This is a curated list of the top hottest"
                                                            f" songs on Billboard top 100 on {date}."
                                                            f" Hope you enjoy this amazing list.", public=False)
        new_list_id = playlist["id"]
        try:
            spotify.playlist_add_items(items=song_uris, playlist_id=new_list_id, position=None)
        except BaseException as e:
            print(e)

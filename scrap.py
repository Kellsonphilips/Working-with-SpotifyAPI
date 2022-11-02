import requests
from bs4 import BeautifulSoup

date = input("What year do you want to travel to? Please, type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100"


response = requests.get(f"{URL}/{date}")
response.raise_for_status()
song_data = response.text


def get_song():
    """
    - Take all website information and return a specific data object needed
    - Return information songs
    :return: WebSite title and song_data needed for spotify search
    """

    soup_in = BeautifulSoup(song_data, "html.parser")
    title = soup_in.title.getText()
    all_songs = soup_in.find_all(name="h3", class_="a-no-trucate")
    song_names = [name.getText().replace("\n", "").replace("\t", "") for name in all_songs]
    return title, song_names


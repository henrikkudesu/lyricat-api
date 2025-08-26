import os
import requests
from bs4 import BeautifulSoup

GENIUS_API_KEY = os.getenv("GENIUS_API_KEY")
BASE_URL = "https://api.genius.com"
HEADERS = {"Authorization": f"Bearer {GENIUS_API_KEY}"}


def search_artist(artist_name: str):
    """Busca um artista pelo nome."""
    response = requests.get(
        f"{BASE_URL}/search",
        headers=HEADERS,
        params={"q": artist_name}
    )
    response.raise_for_status()
    hits = response.json().get("response", {}).get("hits", [])

    if not hits:
        raise ValueError(f"Artista '{artist_name}' não encontrado.")

    return hits[0]["result"]["primary_artist"]


def get_artist_songs(artist: str):
    """Busca TODAS as músicas de um artista no Genius API."""
    artist_data = search_artist(artist)
    artist_id = artist_data["id"]

    url = f"{BASE_URL}/artists/{artist_id}/songs"
    songs = []
    page = 1

    while True:
        response = requests.get(
            url,
            headers=HEADERS,
            params={"page": page, "per_page": 50, "sort": "title"}
        )
        response.raise_for_status()
        data = response.json().get("response", {})
        page_songs = data.get("songs", [])

        if not page_songs:
            break

        for song in page_songs:
            songs.append(song["title"])

        if not data.get("next_page"):
            break

        page += 1

    return songs


def get_lyrics(artist: str, title: str) -> str | None:
    """Busca letra de uma música no Genius (via scraping)."""
    search_response = requests.get(
        f"{BASE_URL}/search",
        headers=HEADERS,
        params={"q": f"{artist} {title}"}
    )
    search_response.raise_for_status()
    hits = search_response.json()["response"]["hits"]

    if not hits:
        return None

    song_url = hits[0]["result"]["url"]

    # Scraping do HTML
    page = requests.get(song_url)
    soup = BeautifulSoup(page.text, "html.parser")

    lyrics_divs = soup.find_all("div", {"data-lyrics-container": "true"})
    lyrics = "\n".join([div.get_text(separator="\n") for div in lyrics_divs])

    return lyrics if lyrics else None

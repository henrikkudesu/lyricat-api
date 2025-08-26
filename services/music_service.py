import os
import requests

GENIUS_API_KEY = os.getenv("GENIUS_API_KEY")
BASE_URL = "https://api.genius.com"

def search_artist(artist_name: str):
    """Busca artistas no Genius API"""
    headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}
    response = requests.get(
        f"{BASE_URL}/search",
        headers=headers,
        params={"q": artist_name}
    )
    response.raise_for_status()
    return response.json()

def get_lyrics(artist: str, title: str) -> str | None:
    """Busca letra de uma música no Genius (simplificado)"""
    headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}

    # 1. Buscar a música pelo nome e artista
    search_response = requests.get(
        f"{BASE_URL}/search",
        headers=headers,
        params={"q": f"{artist} {title}"}
    )
    search_response.raise_for_status()
    hits = search_response.json()["response"]["hits"]

    if not hits:
        return None

    # 2. Pegar a URL da letra
    song_url = hits[0]["result"]["url"]

    # 3. Scraping básico do HTML para extrair a letra
    from bs4 import BeautifulSoup
    page = requests.get(song_url)
    soup = BeautifulSoup(page.text, "html.parser")

    # Genius coloca a letra dentro de <div data-lyrics-container="true">
    lyrics_divs = soup.find_all("div", {"data-lyrics-container": "true"})
    lyrics = "\n".join([div.get_text(separator="\n") for div in lyrics_divs])

    return lyrics if lyrics else None

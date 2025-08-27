import os
import lyricsgenius

GENIUS_API_KEY = os.getenv("GENIUS_API_KEY")

custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

genius = lyricsgenius.Genius(
    GENIUS_API_KEY,
    timeout=15,
    retries=3,
    remove_section_headers=True,
    headers=custom_headers
)

def get_artist_songs(artist_name: str, max_songs: int | None = None):
    artist = genius.search_artist(
        artist_name, 
        max_songs=max_songs or 50, 
        sort="title"
    )
    if not artist or not artist.songs:
        raise ValueError(f"Nenhuma música encontrada para o artista '{artist_name}'.")

    songs_data = []
    for song in artist.songs:
        songs_data.append({
            "title": song.title,
            "album": song.album["name"] if song.album else None,
            "image_url": song.album["cover_art_url"] if song.album else None,
            "url": song.url
        })

    return songs_data


def get_lyrics(artist: str, title: str) -> str:
    song = genius.search_song(title, artist)
    if not song:
        raise ValueError(f"Letra não encontrada para '{title}' de '{artist}'.")
    return song.lyrics

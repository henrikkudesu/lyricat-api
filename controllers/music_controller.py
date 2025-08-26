from services import music_service

def get_artist_songs(artist: str, limit: int = 10):
    return music_service.get_artist_songs(artist)

def find_artist(name: str):
    return music_service.search_artist(name)

def get_lyrics(artist: str, title: str):
    lyrics = music_service.get_lyrics(artist, title)
    if lyrics is None:
        raise ValueError("Letra não encontrada para a música informada.")
    return lyrics
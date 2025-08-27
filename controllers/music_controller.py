from services import music_service

def get_artist_songs(artist: str, max_songs: int):
    return music_service.get_artist_songs(artist, max_songs=max_songs)

def get_lyrics(artist: str, title: str):
    result = music_service.get_lyrics(artist, title)
    if result is None:
        raise ValueError(f"Letra não encontrada para '{title}' de '{artist}'.")
    return result

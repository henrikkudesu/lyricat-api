from services import music_service
from utils import logger

def get_artist_songs(artist: str, max_songs: int):
    logger.info(f"Buscando músicas para o artista '{artist}' com max_songs = {max_songs}")
    try:
        songs = music_service.get_artist_songs(artist, max_songs=max_songs)
        logger.info(f"Foram encontradas {len(songs)} músicas para o artista '{artist}'")
        return songs
    except Exception as e:
        logger.error(f"Erro ao buscar músicas para o artista '{artist}': {e}", exc_info=True)
        raise

def get_lyrics(artist: str, title: str):
    logger.info(f"Buscando letra para a música '{title}' do artista '{artist}'")
    try:
        result = music_service.get_lyrics(artist, title)
        logger.info(f"Letra encontrada para a música '{title}' do artista '{artist}'")
        return result
    except Exception as e:
        logger.error(f"Erro ao buscar letra para a música '{title}' do artista '{artist}': {e}", exc_info=True)
        raise ValueError(f"Letra não encontrada para '{title}' de '{artist}'.")
from services import music_service

def find_artist(name: str):
    # Aqui é possível adicionar lógica adicional, como tratamento de erros ou log
    return music_service.search_artist(name)

def get_lyrics(artist: str, title: str):
    # Validação ou tratamento de exceção se a letra não for encontrada
    lyrics = music_service.get_lyrics(artist, title)
    if lyrics is None:
        raise ValueError("Letra não encontrada para a música informada.")
    return lyrics
from fastapi import APIRouter, Query, HTTPException
from controllers import music_controller
from services.gemini_service import translate_lyrics, explain_lyrics

router = APIRouter()

@router.get("/artist")
def list_artist_songs(
    artist: str = Query(...),
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100)
):
    try:
        songs = music_controller.get_artist_songs(artist)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

    start = (page - 1) * per_page
    end = start + per_page
    paginated = songs[start:end]

    return {
        "artist": artist,
        "page": page,
        "per_page": per_page,
        "total_songs": len(songs),
        "songs": paginated
    }

@router.get("/lyrics/translate")
def translate_song(artist: str = Query(...), title: str = Query(...)):
    try:
        lyrics = music_controller.get_lyrics(artist, title)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    translation = translate_lyrics(lyrics, language="portuguese")
    return {
        "artist": artist,
        "title": title,
        "translation": translation
    }

@router.get("/lyrics/explain")
def explain_song(artist: str = Query(...), title: str = Query(...)):
    try:
        lyrics = music_controller.get_lyrics(artist, title)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    explanation = explain_lyrics(lyrics, language="portuguese")
    return {
        "artist": artist,
        "title": title,
        "explanation": explanation
    }
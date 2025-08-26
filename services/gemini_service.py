from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def translate_lyrics(lyrics: str, language: str = "portuguese") -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Traduza para {language} a seguinte letra de música:\n\n{lyrics}"
    )
    return response.text.strip()

def explain_lyrics(lyrics: str, language: str = "portuguese") -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Explique em {language} o significado cultural, metáforas e gírias da seguinte letra de música:\n\n{lyrics}"
    )
    return response.text.strip()

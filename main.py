from fastapi import FastAPI
from routes import music

app = FastAPI(title="Lyricat API", version="0.1.0")

# registrando rotas
app.include_router(music.router, prefix="/music", tags=["Music"])
## app.include_router(ai.router, prefix="/ai", tags=["IA"])

@app.get("/")
def root():
    return {"message": "API Lyricat rodando 🚀"}

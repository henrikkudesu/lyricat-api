# Lyricat API

A API Lyricat permite traduzir e explicar letras de músicas através de endpoints REST utilizando o FastAPI. Ela se conecta a serviços externos, como a API do Genius para busca de letras e um serviço de IA (Gemini API) para tradução e explicação.

## Estrutura do Projeto

- **main.py:** Arquivo principal para iniciar a aplicação FastAPI.
- **controllers/**: Camada que contém a lógica de negócio, tratamento de erros e validações. Por exemplo, em `controllers/music_controller.py` há funções para buscar letras e tratar erros quando a letra não é encontrada.
- **routes/**: Definição dos endpoints da API. Em `routes/music.py` estão os endpoints para traduzir e explicar letras de músicas.
- **services/**: Responsável pela comunicação com APIs externas, como o Genius e os serviços de IA. Por exemplo, em `services/music_service.py` é feita a busca de letras via API do Genius.
- **utils/**: Funções utilitárias, como tratamento centralizado de erros e logs. (Futuramente)

## Endpoints

### GET /lyrics/translate

Endpoint para traduzir a letra de uma música.

**Parâmetros (query):**

- `artist`: Nome do artista.
- `title`: Título da música.

**Exemplo de chamada:**

```
http://127.0.0.1:8000/lyrics/translate?artist=Eminem&title=Lose%20Yourself
```

**Resposta:**

```json
{
  "artist": "Eminem",
  "title": "Lose Yourself",
  "translation": "Tradução da letra..."
}
```

### GET /lyrics/explain

Endpoint para explicar o significado da letra de uma música.

**Parâmetros (query):**

- `artist`: Nome do artista.
- `title`: Título da música.

**Exemplo de chamada:**

```
http://127.0.0.1:8000/lyrics/explain?artist=Eminem&title=Lose%20Yourself
```

**Resposta:**

```json
{
  "artist": "Eminem",
  "title": "Lose Yourself",
  "explanation": "Explicação da letra..."
}
```

## Configuração

Antes de executar a API, defina as seguintes variáveis de ambiente:

- **GENIUS_API_KEY:** Chave de acesso à API do Genius, usada para buscar letras.
- **GEMINI_API_KEY:** Chave de acesso para serviços do Gemini

**Exemplo (Windows PowerShell):**

```
$env:GENIUS_API_KEY = "sua_chave_aqui"
uvicorn main:app
```

## Execução

### 1. Ativação do Ambiente Virtual

- **Bash / Linux / MacOS:**

  ```bash
  source .venv/bin/activate
  ```

- **PowerShell (Windows):**

  ```powershell
  & .\.venv\Scripts\Activate.ps1
  ```

### 2. Iniciar o Servidor FastAPI com UV

```bash
uv run uvicorn main:app --reload
```

### 3. Acesse a Documentação Interativa da API (Swagger)

Abra seu navegador e acesse:

```
http://127.0.0.1:8000/docs
```

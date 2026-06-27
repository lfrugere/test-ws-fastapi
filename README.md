# test-ws-fastapi

Projet FastAPI géré par `uv`, compatible Python 3.12.

## Installation

```powershell
uv sync
```

## Lancement

Commande recommandée :

```powershell
uv run start-api
```

Cette commande lance l'API sur :

[http://localhost:3000](http://localhost:3000)

Commande équivalente explicite :

```powershell
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 3000
```

Si le port `8080` est disponible sur votre poste, vous pouvez aussi lancer :

```powershell
uv run uvicorn app.main:app --reload --port 8080
```

Documentation interactive :

[http://localhost:3000/docs](http://localhost:3000/docs)

## Configuration

Créez un fichier `.env` à partir de `.env.example`, puis adaptez les clés.

Format attendu :

```env
API_KEYS=app_denodo:denodo-secret-key,app_batch:batch-secret-key
```

Le fichier `.env` est ignoré par Git afin de ne pas stocker de secrets dans
le dépôt.

## Exemple curl

```powershell
curl -H "X-API-Key: denodo-secret-key" `
  http://localhost:3000/hello/Lionel
```

Réponse :

```json
{
  "message": "Hello Lionel",
  "client_app": "app_denodo"
}
```

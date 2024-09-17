from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
import uuid
import httpx
from datetime import datetime, timedelta

app = FastAPI()

# Хранилище для URL-ов с добавлением срока действия
url_store = {}


class URLRequest(BaseModel):
    url: HttpUrl
    expiration: int = 60  # Время действия ссылки в минутах (по умолчанию 1 час)


@app.post("/", status_code=201)
async def create_short_url(request: URLRequest):
    # Генерация уникального идентификатора для сокращенного URL
    short_id = str(uuid.uuid4())[:6]
    expiration_time = datetime.utcnow() + timedelta(minutes=request.expiration)
    url_store[short_id] = {"url": request.url, "expires": expiration_time}
    return {"short_url_id": short_id, "expiration_time": expiration_time}


@app.get("/{short_id}")
async def redirect_to_url(short_id: str):
    # Проверка, существует ли сокращенный URL
    if short_id not in url_store:
        raise HTTPException(status_code=404, detail="Short URL not found")

    url_data = url_store[short_id]

    # Проверка, не истек ли срок действия
    if datetime.utcnow() > url_data["expires"]:
        raise HTTPException(status_code=410, detail="Short URL has expired")

    original_url = url_data["url"]
    return RedirectResponse(original_url)


@app.get("/async-data/")
async def get_async_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
        return response.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)

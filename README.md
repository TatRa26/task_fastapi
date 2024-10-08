# Task API на FastAPI


Этот проект представляет собой простое API для сокращения URL с использованием FastAPI. Пользователи могут создавать сокращенные URL-адреса с указанием срока действия. API также поддерживает асинхронный запрос данных из внешнего API.

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone <repository_url>
cd <repository_folder>
Установите зависимости:
bash
Копировать код
pip install -r requirements.txt
Запустите приложение:
bash
Копировать код
uvicorn main:app --reload
Описание API
POST /
Создает новый сокращенный URL с указанием срока действия.

URL: /
Метод: POST
Тело запроса:
url (обязательный) — оригинальный URL, который нужно сократить.
expiration (необязательный) — срок действия в минутах (по умолчанию 60 минут).
Пример запроса:
json
Копировать код
{
  "url": "https://example.com",
  "expiration": 30
}
Пример ответа:
json
Копировать код
{
  "short_url_id": "abc123",
  "expiration_time": "2024-09-17T10:15:30.000Z"
}
GET /{short_id}
Перенаправляет на оригинальный URL, если срок действия еще не истек.

URL: /{short_id}
Метод: GET
Параметры пути:
short_id — уникальный идентификатор сокращенного URL.
Пример ответа:
Если ссылка действительна: перенаправление на оригинальный URL.
Если ссылка не найдена: возвращает ошибку 404.
Если ссылка просрочена: возвращает ошибку 410.
GET /async-data/
Асинхронный запрос данных с внешнего API.

URL: /async-data/
Метод: GET
Пример ответа:
json
Копировать код
{
  "data": {...}
}
Хранилище URL-адресов
URL-адреса сохраняются в переменной url_store в формате словаря Python, где ключ — это сокращенный ID, а значение — это оригинальный URL и время его истечения. Пример структуры:

python
Копировать код
url_store = {
    "abc123": {"url": "https://example.com", "expires": datetime(2024, 9, 17, 10, 15, 30)}
}
Асинхронность
API использует асинхронные возможности FastAPI для работы с внешними API через библиотеку httpx.

Запуск приложения
Приложение можно запустить с помощью Uvicorn:

bash
Копировать код
uvicorn main:app --host 127.0.0.1 --port 8080
Зависимости
FastAPI
Uvicorn
HTTPX
Pydantic
Лицензия
Этот проект распространяется под MIT лицензией.











# Проект Коллекция мемов"
Данный проект представляет собой веб-приложение на Python, с использованием FastAPI, которое предоставляет API для работы с коллекцией мемов.
### Описание
Приложение состоит из двух сервисов: сервис с публичным API с бизнес-логикой и сервис для работы с медиа-файлами, используя S3-совместимое хранилище MinIO.
### Возможности проекта
- GET /memes: Получить список всех мемов (с пагинацией).
- GET /memes/{id}: Получить конкретный мем по его ID.
- POST /memes: Добавить новый мем (с картинкой и текстом).
- PUT /memes/{id}: Обновить существующий мем.                                        
- DELETE /memes/{id}: Удалить мем.
### Запуск проекта
1. Клонируйте репозиторий - [github.com](https://github.com/vvd2209/Collection_memes).
2. Запустите сервисы с помощью Docker Compose командой - docker-compose build.
3. Запустите сервер командой - uvicorn app.main:app --reload .
4. API будет доступно по адресу: http://localhost:8000.
5. Для запуска тестов используйте команду - pytest.
6. Документация API доступна по адресу http://127.0.0.1:8000/docs.
### Docker
Для создания образа из Dockerfile запустите команду **docker-compose build**

Для запуска контейнера используйте команду **docker-compose up**

Для остановки контейнера используйте команду **docker-compose down**

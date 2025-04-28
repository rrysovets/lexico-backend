Language Learning API
Проект представляет собой RESTful API для приложения по изучению иностранных языков с функционалом словаря. 
Построен на Django REST Framework с использованием PostgreSQL и Redis.

# 🚀 Быстрый старт
## Требования
Docker и Docker Compose

Python 3.9+ (для запуска без Docker)

## Установка
Скопируйте файл окружения:

bash
cp .env.template .env
Заполните .env своими значениями

## Запустите сервисы:

bash
make up
## 🛠 Управление проектом
Команда	Описание	Пример использования
make help	Показать все доступные команды	make help
make up	Запустить сервисы в фоновом режиме	make up
make down	Остановить все сервисы	make down
make build	Пересобрать контейнеры	make build
make logs	Просмотр логов в реальном времени	make logs
## 📡 API Endpoints
Модули обучения
Пример объекта модуля
json
{
    "id": 3,
    "title": "Животные",
    "dictionary": {
        "cat": "кот",
        "dog": "собака",
        "fox": "лиса",
        "owl": "сова",
        "bear": "медведь",
        "deer": "олень"
    },
    "is_public": false,
    "created_at": "2023-01-01T12:00:00Z"
}
Получить список модулей
GET /api/modules/
Ответ: Массив объектов модулей

Создать новый модуль
POST /api/modules/
Тело запроса:

json
{
    "title": "Новый модуль",
    "dictionary": {
        "hello": "привет",
        "goodbye": "пока"
    },
    "is_public": true
}
Получить конкретный модуль
GET /api/modules/<id>/
Обновить модуль
PUT /api/modules/<id>/
Тело запроса:

json
{
    "title": "Обновлённые животные",
    "dictionary": {
        "whale": "кит",
        "shark": "акула"
    }
}
Удалить модуль
DELETE /api/modules/<id>/
## 📚 Особенности формата
dictionary - словарь в формате {"слово": "перевод"}:

Минимум 5 пар слов

Пустые значения запрещены

Регистрозависимый

is_public - флаг публичности модуля:

true - доступен всем пользователям

false - доступен только автору

## 🔒 Переменные окружения
ini
# Django
DJANGO_SECRET_KEY='your-secret-key'

# PostgreSQL
POSTGRES_NAME=db_name
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Redis
REDIS_PASSWORD=redis_pass
REDIS_USER=default
REDIS_USER_PASSWORD=user_pass
⚠️ Безопасность
Все чувствительные данные хранятся в .env

Используйте HTTPS в production

Регулярно делайте бэкапы БД

Обновляйте зависимости


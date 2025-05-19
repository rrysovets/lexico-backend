LEXICO API
Проект представляет собой RESTful API для приложения по изучению иностранных языков с функционалом словаря. 
Построен на Django REST Framework с использованием PostgreSQL и Redis.

# 🚀 Быстрый старт
## Требования
- Docker и Docker Compose
- Python 3.9+ (для запуска без Docker)

## Установка
1. Скопируйте файл окружения:
```bash
cp env.template .env
```
2. Заполните `.env` своими значениями

## Запуск сервисов
```bash
make up
```

## 🛠 Управление проектом
| Команда | Описание | Пример использования |
|---------|----------|---------------------|
| make help | Показать все доступные команды | make help |
| make up | Запустить сервисы в фоновом режиме | make up |
| make down | Остановить все сервисы | make down |
| make build | Пересобрать контейнеры | make build |
| make logs | Просмотр логов в реальном времени | make logs |

## 📡 API Endpoints

### Аутентификация
API использует токен-аутентификацию. Все запросы (кроме публичных) должны содержать заголовок:
```
Authorization: Token your-auth-token
```

### Модули обучения

#### Пример объекта модуля
```json
{
    "id": 3,
    "title": "Животные",
    "dictionary": {
        "cat": "кот",
        "dog": "собака",
        "fox": "лиса"
    },
    "is_public": false,
    "author": "username",
    "created_at": "2023-01-01T12:00:00Z",
    "updated_at": "2023-01-01T12:00:00Z",
    "rating": 5,
    "is_liked": false
}
```

#### Получить список модулей
```
GET /api/v1/modules/
```
Возвращает массив объектов модулей. Поддерживает пагинацию (10 элементов на страницу).

Параметры фильтрации:
- `is_public` - фильтр по публичности (true/false)
- `search` - поиск по названию
- `ordering` - сортировка (created_at, updated_at, title)

#### Создать новый модуль
```
POST /api/v1/modules/
```
Тело запроса:
```json
{
    "title": "Новый модуль",
    "dictionary": {
        "hello": "привет",
        "goodbye": "пока"
    },
    "is_public": true
}
```

#### Получить конкретный модуль
```
GET /api/v1/modules/{id}/
```

#### Обновить модуль
```
PUT /api/v1/modules/{id}/
```
Тело запроса аналогично созданию модуля.

#### Удалить модуль
```
DELETE /api/v1/modules/{id}/
```

#### Поставить/убрать лайк модулю
```
POST /api/v1/modules/{id}/toggle_like/
```
Ответ:
```json
{
    "rating": 6,
    "liked": true
}
```

### Генерация модулей с помощью AI

#### Запустить генерацию
```
POST /api/v1/generate-theme?theme=animals&count_of_words=10
```
Ответ:
```json
{
    "task_id": "task-uuid"
}
```

#### Получить результат генерации
```
GET /api/v1/generate-theme-result/{task_id}
```
Ответ:
```json
{
    "status": "success",
    "data": {
        "title": "Animals",
        "dictionary": {
            "cat": "кот",
            "dog": "собака"
            // ... другие слова
        }
    }
}
```

## 📚 Особенности и валидация

### Словарь (dictionary)
- Формат: `{"слово": "перевод"}`
- Ключи и значения должны быть строками
- Пустые значения запрещены
- Регистрозависимый

### Видимость модуля (is_public)
- `true` - доступен всем пользователям
- `false` - доступен только автору

## 🔒 Переменные окружения
```ini
# Django Settings
DJANGO_SECRET_KEY='your-secret-key-here'
AI_API_KEY=your-api-key

# PostgreSQL Database Settings
POSTGRES_NAME=your_database_name
POSTGRES_USER=your_database_user
POSTGRES_PASSWORD=your_database_password
POSTGRES_HOST=your_database_host
POSTGRES_PORT=your_database_port

# Redis Settings
REDIS_PASSWORD=your_redis_password
REDIS_USER=your_redis_user
REDIS_USER_PASSWORD=your_redis_user_password
```

## ⚠️ Безопасность
- Все чувствительные данные хранятся в `.env`
- Используйте HTTPS в production
- Регулярно делайте бэкапы БД
- Обновляйте зависимости

## 📝 Лицензия

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для деталей.

Copyright (c) 2024 LEXICO


# 🏡 Projectich — Система аренды жилья

**Projectich** — это полнофункциональное backend-приложение на Django для размещения, поиска и бронирования жилья. Поддерживает регистрацию пользователей, систему ролей, отзывы, историю просмотров и поисков, контейнеризацию с Docker и развертывание на сервере.

---

## 🚀 Функциональность

### 📋 Объявления
- ✅ Создание, редактирование, удаление объявлений
- ✅ Управление доступностью (активно/неактивно)
- ✅ Поля: заголовок, описание, цена, город, тип жилья, количество комнат

### 🔍 Поиск и фильтрация
- 🔎 Поиск по ключевым словам (заголовок и описание)
- 🔧 Фильтрация: цена, количество комнат, тип, город
- 🔁 Сортировка: по дате, цене, популярности

### 👤 Аутентификация и авторизация
- ✅ Регистрация и вход
- 🔐 Разграничение прав: арендатор / арендодатель

### 📅 Бронирования
- 📌 Создание и отмена брони
- 🕓 Подтверждение/отклонение брони арендодателем
- 📑 Просмотр истории бронирований

### ⭐ Рейтинги и отзывы
- 📝 Оставление отзыва и рейтинга после аренды
- 👀 Просмотр отзывов по объявлению

### 📊 Аналитика и история
- 👁️ Учёт просмотров и популярных объявлений
- 🔎 История поисков и популярных запросов

---

## ⚙️ Технологии

- 🐍 Django + Django REST Framework
- 🐬 MySQL 8
- 🐳 Docker / Docker Compose
- 🌍 Swagger (drf-spectacular)
- ☁️ (Готово к развертыванию на AWS EC2)

---

## 🐳 Быстрый старт с Docker

### 1. Клонируй репозиторий:
```bash
git clone https://github.com/your-user/projectich.git
cd projectich
```

### 2. Создай `.env` файл:
```env
MYSQL_DATABASE=projectich_db
MYSQL_USER=admin
MYSQL_PASSWORD=admin
MYSQL_ROOT_PASSWORD=root
DJANGO_SECRET_KEY=domik
DEBUG=True
```

### 3. Запусти проект:
```bash
docker-compose up --build
```

### 4. Открой в браузере:
- Django сайт: [http://localhost:8000](http://localhost:8000)
- Swagger документация: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/) (если включено)

---

## 🧪 Примеры JSON-запросов

### Регистрация
```json
POST /api/users/register/
{
  "email": "user@example.com",
  "password": "string",
  "full_name": "John Doe",
  "role": "tenant"
}
```

### Создание объявления
```json
POST /api/listings/
{
  "title": "Уютная квартира в Берлине",
  "description": "Сдаю квартиру недалеко от центра",
  "price": 500,
  "city": "Berlin",
  "room_count": 2,
  "property_type": "apartment",
  "is_active": true
}
```

### Поиск жилья
```json
GET /api/listings/?search=Берлин&min_price=400&max_price=600&rooms=2
```

### Бронирование
```json
POST /api/bookings/
{
  "listing_id": 1,
  "start_date": "2025-06-10",
  "end_date": "2025-06-14"
}
```

### Оставить отзыв
```json
POST /api/reviews/
{
  "listing_id": 1,
  "rating": 5,
  "comment": "Отличное жильё!"
}
```

---

## 🧠 Что рассказать на защите

1. **Что делает проект** — аренда, поиск, бронирование, отзывы.
2. **Как устроен** — Django backend, REST API, Docker, MySQL.
3. **Что ты сделал** — реализация всех этапов ТЗ, тестирование, запуск в Docker.
4. **Что можно улучшить** — фронт, фильтрация по дате, оплата, вывод средств, ElasticSearch.
5. **Покажи Swagger** — и через него сделай:
   - регистрацию
   - создание объявления
   - поиск
   - бронирование
   - отзыв

---

## ✅ Статус проекта

✅ Полностью реализован и готов к защите

---

## 📦 Автор

Hasanov Dominik
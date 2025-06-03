# Projectich — система аренды жилья

## Описание
Полнофункциональное backend-приложение для аренды жилья с объявлениями, бронированием, отзывами и системой аналитики.

## Стек технологий
- Python 3.12
- Django 5.2
- Django REST Framework
- MySQL
- Docker
- AWS (EC2 — по желанию)

## Как развернуть проект

1. Клонируйте репозиторий:
git clone <URL>
cd projectich

2. Установите зависимости:
pip install -r requirements.txt

3. Настройте `.env` файл или переменные окружения:
DB_HOST=localhost
DB_NAME=projectich_db
DB_USER=admin
DB_PASSWORD=yourpassword


4. Выполните миграции:
python manage.py migrate

5. Запустите сервер:
python manage.py runserver

6. Перейдите в браузере:
http://127.0.0.1:8000/api/docs/


---

#### 2. **Тестовые учётные данные**
В конце `README.md` добавь блок:

```markdown
## Тестовые пользователи

**Арендодатель:**
- username: adminuser
- password: admin123

**Арендатор:**
- username: tenantuser
- password: tenant123

Django OTP Authentication API

Это учебный проект на Django, реализующий систему авторизации через одноразовые пароли (OTP) с выдачей JWT-токена.

Автор: koxnokrcromxvnpp

Стек технологий: Python 3.x, Django, Django REST Framework, SimpleJWT.
🚀 Функционал

    Отправка OTP: Принимает email, генерирует 6-значный код и сохраняет его в базе данных (время жизни — 5 минут).

    Проверка OTP: Проверяет код. Если код верный и не просрочен, активирует пользователя.

    JWT Авторизация: После успешной проверки возвращает access и refresh токены для доступа к защищенным ресурсам.

🛠 Установка и запуск
1. Клонирование репозитория
Bash

git clone <ссылка_на_ваш_репозиторий>
cd my_otp_project

2. Настройка виртуального окружения
Bash

# Создание
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Активация (macOS/Linux)
source venv/bin/activate

3. Установка зависимостей
Bash

pip install django djangorestframework djangorestframework-simplejwt django-cors-headers

4. Миграции базы данных
Bash

python manage.py makemigrations
python manage.py migrate

5. Запуск сервера
Bash

python manage.py runserver

📑 Документация API
1. Отправка OTP

    URL: /auth/send-otp

    Метод: POST

    Тело запроса:

JSON

{
  "email": "user@example.com"
}

    Примечание: Так как это демо-версия, код не отправляется на почту, а выводится в терминал (консоль), где запущен сервер.

2. Проверка OTP

    URL: /auth/verify-otp

    Метод: POST

    Тело запроса:

JSON

{
  "email": "user@example.com",
  "code": "123456"
}

    Ответ (успех):

JSON

{
  "refresh": "eyJhbG...",
  "access": "eyJhbG..."
}

📂 Структура проекта

    core/ — основные настройки (settings, urls).

    accounts/ — приложение для работы с пользователями и OTP.

        models.py — модель OTP с логикой проверки времени жизни.

        views.py — логика обработки запросов.

    db.sqlite3 — локальная база данных.


    adfs

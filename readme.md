## Тестовое задание

### Доступные инструменты:
- Python >=3.5
- Django >=1.11
- SQLLite (для хранения данных)
- python-requests (для получения тестовых данных)
- Bootstrap >=3 (по желанию)
- js, css, html

### Тестовые данные:
- пользователи: http://jsonplaceholder.typicode.com/users
- посты: http://jsonplaceholder.typicode.com/posts

### Задание:
1. Автоматизировать загрузку в локальную БД данных пользователей и постов.
2. Реализовать отображение (через Web) страницы с таблицей.


## Документация по проекту

Для запуска проекта необходимо

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

- Команда для загрузки в БД данных о пользователях

```bash
python manage.py import_users
```

- Команда для загрузки в БД постов пользователей

```bash
python manage.py import_posts
```

- Команда для запуска приложения

```bash
python manage.py runserver
```
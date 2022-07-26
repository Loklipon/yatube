# **YaTube**

### _Описание проекта_
Проект YaTube позволяет создать учетную запись, публиковать посты, редактировать их, подписываться на любымых авторов, а также оставлять комментарии. В работе с учетной записью имеется возможность менять пароль, а также производить процедуру восстановления пароля путем отправки письма на почту.

Также в проекте реализовано API*

### _Как запустить проект (Windows)_ 
* Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Loklipon/api_yamdb
```
```
cd api_yamdb
```
* Создать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Script/activate
```
* Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
* Перейти в папку api_yamdb, и выполнить миграции:
```
cd api_yamdb
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
* Запустить проект:
```
python3 manage.py runserver
```

### _Технологии, использованные в процессе создания проекта_
- Python 3.7
- Django 2.2.16
- DjangoRestFramework 3.12.4
- DjangoFilter 2.4.0
- Pytest 6.2.4
- SQLite
- Simple JWT

---
*После запуска проекта по адресу http://127.0.0.1:8000/redoc/ будет доступна документация. В ней описаны всевозможные запросы к API, которые должны были быть реализовны в проекте. Документация в ReDoc.

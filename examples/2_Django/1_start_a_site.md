# Start a site

## install django

```shell
pip install django
```

## startproject

```shell
cd <project_root_directory>
django-admin startproject mysite  # 'mysite' can be changed into any name you like, but i still prefer mysite
```

then you should get

```shell
mysite/
    manage.py  # important file!
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## testproject

```shell
python manage.py runserver 0.0.0.0:8080
```

## a project can have multiple apps that works together

```shell
python manage.py startapp polls
```

## reading order

1. polls/views.py
2. polls/urls.py
3. mysite/urls.py
4. mysite/settings.py 修改TIME_ZONE = 'Asia/Shanghai'
5. polls/models.py (这个是为了数据库, 可略过)
6. mysite/settings.py 主要看INSTALLED_APPS那一项, (为了数据库, 可略过)
7. polls/admin.py (为了数据库, 可略过)
8. polls/views.py
9. polls/urls.py
10. polls/templates/polls/index.html
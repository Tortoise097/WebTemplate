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
python manage.py startalp polls
```




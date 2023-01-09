## Installation

Для запуска приложения требуется [Python 3.10](https://www.python.org/downloads/release/python-3104/).

Установите зависимости и запустите сервер.

***

### Установка питонячих зависимостей

```sh
cd photo_m
pip install -r requirements.txt
```

***

## Запуск

```sh
python manage.py runserver
```

***

```sh
ADMIN_PANEL_LOGIN = admin
ADMIN_PANEL_PASS = admin
```


## Запросы

### CREATE Image

![Alt text](for_readme/create_iamge.png?raw=true "Create")

```sh
image - REQUIRED
name - OPTIONAL [separator=', ']
location - OPTIONAL
description - OPTIONAL
```

### GET Images

```sh
url = http://127.0.0.1:8000/api/images/
```

### GET Image

```sh
url = http://127.0.0.1:8000/api/images/<image_id>/
```

### FILTER Images

```sh
url = http://127.0.0.1:8000/api/images/?name=Test&location=Test&description=Test

name - OPTIONAL
location - OPTIONAL
description - OPTIONAL
```


### SEARCH Names

```sh
url = http://127.0.0.1:8000/api/persons/?name=Test

name - REQUIRED
```
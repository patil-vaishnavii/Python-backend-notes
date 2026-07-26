# Django Learning Notes

> These are my personal notes while learning Django.

---

# Django Project Structure

There are **3 levels** in a Django project:

## 1. Root Level

This is the main project folder that contains everything.

Example:

```
First-Django-Project/
│── manage.py
│── db.sqlite3
│── MeandDjango/
│── home/
```

### Files

### `manage.py`

- Entry point for Django commands.
- Used to run the server, create apps, migrations, etc.

Common commands:

```bash
python manage.py runserver
python manage.py startapp home
python manage.py makemigrations
python manage.py migrate
```

---

### `db.sqlite3`

- Default database provided by Django.
- Automatically created after running migrations.
- Good for development and learning.
- Can later be replaced with MySQL, PostgreSQL, etc.

---

# 2. Project Level

Example:

```
MeandDjango/
```

This folder controls the **entire Django project**.

Important files:

- `settings.py`
- `urls.py`
- `wsgi.py`
- `asgi.py`

## `settings.py`

Project configuration file.

Contains:

- Installed Apps
- Database settings
- Templates
- Static files
- Security settings

Example:

```python
INSTALLED_APPS = [
    "home",
]
```

---

## `urls.py`

The **main URL dispatcher**.

Receives every request first and sends it to the appropriate app.

Example:

```python
urlpatterns = [
    path("", include("home.urls")),
]
```

---

# 3. App Level

Example:

```
home/
```

Apps contain the actual functionality of your website.

Important files:

- `views.py`
- `urls.py`
- `models.py`
- `admin.py`

---

# views.py

Contains the logic for each page.

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World! Homepage")
```

### Explanation

- Browser sends a request.
- Django calls this function.
- The function returns a response to the browser.

---

# Django Request Flow

```
Browser

↓

Project urls.py

↓

App urls.py

↓

views.py

↓

Template

↓

Browser
```

Whenever confused, ask yourself:

> **"Where is my request right now?"**

---

# Templates

Templates are HTML files that Django sends to the browser.

Usually stored inside a folder named:

```
templates/
```

Example:

```
home/
    templates/
        home/
            index.html
```

Instead of writing HTML inside Python, Django renders template files.

Example:

```python
return render(request, "home/index.html")
```

---

# render()

Import:

```python
from django.shortcuts import render
```

Purpose:

- Loads an HTML template.
- Sends it to the browser.

---

# HttpResponse

Import:

```python
from django.http import HttpResponse
```

Purpose:

Returns plain text directly.

Example:

```python
return HttpResponse("Hello World")
```

---

# Django Template Language (DTL)

Django uses its own templating language.

### Variables

Use:

```html
{{ variable }}
```

Example:

```html
<h1>{{ username }}</h1>
```

---

### Template Tags

Use:

```html
{% %}
```

Example:

```html
{% if user %}
```

---

# Static Files

Static files include:

- CSS
- JavaScript
- Images

Load static files using:

```html
{% load static %}
```

Example:

```html
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

---

# Static Settings

In `settings.py`

```python
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = "static/"
```

### Meaning

`STATIC_URL`

- URL prefix for static files.

`BASE_DIR`

- Points to the project's root directory.

---

# Jinja vs Django Templates

Django uses **Django Template Language (DTL)** by default.

- Inspired by Jinja2.
- No additional installation is needed for normal Django projects.

---

# Django Apps

A Django project can contain **multiple apps**.

Example:

```
Job Portal

├── accounts
├── jobs
├── employers
├── applicants
└── payments
```

Each app is responsible for one feature.

This makes projects modular and easier to manage.

---

# Creating a New App

Command:

```bash
python manage.py startapp home
```

Example:

```bash
python manage.py startapp jobs
```

---

# Things to Remember

✅ Django projects can have multiple apps.

✅ `manage.py` is used to run Django commands.

✅ `db.sqlite3` is Django's default database.

✅ `views.py` contains business logic.

✅ `urls.py` connects URLs to views.

✅ Templates contain HTML.

✅ `render()` loads HTML templates.

✅ `HttpResponse()` returns plain text.

✅ `{{ }}` displays variables.

✅ `{% %}` is used for template logic.

✅ `{% load static %}` enables static files.

✅ `STATIC_URL` defines the URL for static files.

---

# Learning Checklist

- [x] Created a virtual environment
- [x] Installed Django
- [x] Created a Django project
- [x] Started the development server
- [x] Created my first app
- [x] Understood project structure
- [x] Learned `manage.py`
- [x] Learned `settings.py`
- [x] Learned `urls.py`
- [x] Learned `views.py`
- [x] Learned templates
- [x] Learned static files
# Django Learning Notes

# 1. Django Project Settings (`settings.py`)

The `settings.py` file contains the configuration of the entire Django project.

Examples:
# Django `settings.py` Concepts

This document explains some of the most commonly used settings in Django's `settings.py` file, along with their purpose and how they are used in the **FoodVerse** project.

---

# 1. INSTALLED_APPS

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'restaurants',
    'accounts',
]
```

## Definition

`INSTALLED_APPS` is a list of all Django applications that are active in the project.

## Purpose

It tells Django:

> "These are the apps whose models, templates, admin configuration, migrations, and other components should be included in the project."

## In FoodVerse

Custom applications:

* `restaurants`
* `accounts`

Without adding these apps to `INSTALLED_APPS`:

* Models won't be detected.
* Migrations won't be created.
* Admin panel won't recognize the models.
* Templates inside app folders won't be discovered properly.

---

# 2. DATABASES

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

## Definition

The `DATABASES` setting tells Django which database to use and how to connect to it.

## Purpose

Stores all application data, such as:

* Users
* Restaurants
* Menu Items
* Orders (future)
* Authentication data

## In FoodVerse

Database used:

* SQLite

Database file:

```
backend/db.sqlite3
```

When we run:

```bash
python manage.py migrate
```

Django creates database tables inside `db.sqlite3`.

---

# 3. MIDDLEWARE

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]
```

## Definition

Middleware is software that processes every request before it reaches the view and every response before it is sent back to the browser.

Think of middleware as a checkpoint between the browser and your Django application.

## Purpose

Middleware handles:

* Security
* Sessions
* Authentication
* CSRF Protection
* Messages

## In FoodVerse

When a user logs in:

```
Browser
    ↓
Authentication Middleware
    ↓
User becomes authenticated
    ↓
Views can access request.user
```

Without `AuthenticationMiddleware`, Django would not know which user is currently logged in.

---

# 4. TEMPLATES

```python
TEMPLATES = [
    {
        "DIRS": [BASE_DIR / "frontend" / "templates"],
        "APP_DIRS": True,
    }
]
```

## Definition

The `TEMPLATES` setting tells Django where HTML template files are stored.

## Purpose

Whenever a view renders a page, Django searches these directories for the required HTML file.

Example:

```python
return render(request, "restaurants/restaurant_list.html")
```

## In FoodVerse

Common templates:

```
frontend/templates/
```

App-specific templates:

```
accounts/templates/accounts/
restaurants/templates/restaurants/
```

Because:

```python
APP_DIRS = True
```

Django automatically searches the `templates` folder inside every installed app.

---

# 5. STATIC FILES

```python
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "frontend" / "static"
]
```

## Definition

Static files are files that do not change dynamically.

Examples:

* CSS
* JavaScript
* Images
* Icons

## Purpose

Static files are used to style and enhance the website.

## In FoodVerse

CSS file:

```
frontend/static/css/style.css
```

Loaded in HTML using:

```html
{% load static %}

<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

---

# 6. TIME_ZONE

```python
TIME_ZONE = "Asia/Kolkata"
```

## Definition

Specifies the default time zone used by the Django project.

## Purpose

Whenever Django stores or displays date and time, it uses this time zone.

## In FoodVerse

If a model contains:

```python
created_at = models.DateTimeField(auto_now_add=True)
```

The stored timestamp follows the configured time zone (`Asia/Kolkata`).

---

# 7. LANGUAGE_CODE

```python
LANGUAGE_CODE = "en-us"
```

## Definition

Specifies the default language of the Django application.

## Purpose

Controls the language used for Django's built-in interface and messages.

Examples:

* Admin panel
* Form validation messages
* Authentication messages

## In FoodVerse

Current language:

```
English (US)
```

If changed to another supported language, Django's built-in interface and messages would appear in that language where translations are available.

---

# Quick Interview Revision

| Setting            | Definition                                 | Purpose                                                                                 | FoodVerse Example                               |
| ------------------ | ------------------------------------------ | --------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **INSTALLED_APPS** | Registers all active Django applications   | Allows Django to recognize apps, models, templates, migrations, and admin configuration | `accounts`, `restaurants`                       |
| **DATABASES**      | Configures the database connection         | Stores project data                                                                     | SQLite (`backend/db.sqlite3`)                   |
| **MIDDLEWARE**     | Processes every request and response       | Handles security, authentication, sessions, CSRF, and messages                          | Authentication and session handling             |
| **TEMPLATES**      | Specifies where HTML templates are located | Renders HTML pages                                                                      | `frontend/templates` and app-specific templates |
| **STATICFILES**    | Specifies where static assets are stored   | Serves CSS, JavaScript, and images                                                      | `frontend/static/css/style.css`                 |
| **TIME_ZONE**      | Sets the default project time zone         | Ensures consistent date and time handling                                               | `Asia/Kolkata`                                  |
| **LANGUAGE_CODE**  | Sets the default language                  | Controls Django's built-in interface language                                           | `en-us`                                         |

---

# Easy Way to Remember

* **INSTALLED_APPS** → What features does my project have?
* **DATABASES** → Where is my data stored?
* **MIDDLEWARE** → What should happen to every request and response?
* **TEMPLATES** → Where are my HTML files?
* **STATICFILES** → Where are my CSS, JavaScript, and images?
* **TIME_ZONE** → Which time should Django use?
* **LANGUAGE_CODE** → Which language should Django use?


---

## INSTALLED_APPS

Django only recognizes the apps that are registered in `INSTALLED_APPS`.

Example:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    ...
    "todo",
]
```

### Organizing Apps

Instead of writing every app directly inside `INSTALLED_APPS`, we can organize them.

```python
EXTERNAL_APPS = [
    "todo",
]

INSTALLED_APPS += EXTERNAL_APPS
```

### Why use this?

- Makes `settings.py` cleaner.
- Easy to separate Django's default apps from our own apps.
- Helpful when the project becomes large.

---

# 2. Main Logic and Routing

## views.py

**Purpose:** Contains the application's business logic.

Responsibilities:
- Receives request from the user.
- Processes data.
- Communicates with the database.
- Returns a response.

Example:

```python
def home(request):
    ...
```

Think of it as:

```
Request
   ↓
views.py
   ↓
Response
```

---

## urls.py

**Purpose:** Routing

Responsibilities:
- Connects URL to a particular view.

Example:

```python
path("", views.home, name="home")
```

Think of it as:

```
User visits URL
        ↓
urls.py
        ↓
Corresponding View
```

---

# 3. Migrations

## Definition

A migration is Django's way of applying changes made to models into the database.

Whenever we modify a model (create a model, add a field, remove a field, rename a field), Django creates migration files.

Migration files act like version history for the database schema.

---

## Migration Commands

### 1. Create migration files

```bash
python manage.py makemigrations
```

What it does:

- Checks all models.
- Detects changes.
- Generates migration files inside:

```
app_name/
    migrations/
```

Example:

```
0001_initial.py
0002_add_age_field.py
```

**Important:**

`makemigrations` DOES NOT change the database.

It only creates instructions for the database.

---

### 2. Apply migrations

```bash
python manage.py migrate
```

What it does:

- Reads all pending migration files.
- Executes SQL queries.
- Updates the database schema.

This command actually changes the database.

---

## Difference

### makemigrations

```
Models
   ↓
Migration File
```

No database changes happen.

---

### migrate

```
Migration File
      ↓
Database
```

Database is updated.

---

# 4. How does Django know what changed?

Question:

How does Django know which changes were made in the models?

Answer:

Django keeps a history of all migrations.

When `makemigrations` is executed:

1. Django loads all previous migration files.
2. Internally reconstructs the previous state of every model.
3. Compares the previous state with the current models.
4. Detects differences.
5. Creates a new migration only if changes exist.

If there are no differences, Django displays:

```
No changes detected
```

When `migrate` is executed:

- Django checks which migrations have already been applied.
- Information is stored inside the database table:

```
django_migrations
```

Only unapplied migrations are executed.

---

## Common Beginner Confusion

Deleting migration files does **not** delete database changes.

Migration files and the database are two different things.

Deleting migration files incorrectly may cause migration inconsistencies.

---

# 5. Context Dictionary

Context is a dictionary used to send data from a Django view to an HTML template.

Example:

```python
context = {
    "tasks": tasks,
}
```

Passing context:

```python
return render(request, "todo.html", context)
```

Accessing inside template:

```html
{{ tasks }}
```

Think of it like this:

```
views.py
    ↓
context dictionary
    ↓
HTML template
```

Without context, the HTML template cannot access Python variables.

---

# 6. Template Tags

Template tags allow us to write Django logic inside HTML.

Syntax:

```html
{% ... %}
```

Examples:

### Loop

```html
{% for task in tasks %}
{% endfor %}
```

### If

```html
{% if tasks %}
{% endif %}
```

### Load static files

```html
{% load static %}
```

### URL tag

```html
{% url 'delete_task' task.id %}
```

Purpose:
- Generates URLs dynamically.
- Avoids hardcoding URLs.

---

# Quick Revision

## settings.py

- Project configuration
- Register apps
- Configure database
- Configure templates

---

## views.py

Contains application logic.

---

## urls.py

Maps URL → View.

---

## makemigrations

Creates migration files.

Does NOT modify the database.

---

## migrate

Executes migration files.

Updates the database.

---

## Context

Used to pass Python data to HTML templates.

---

## Template Tags

Allow Django logic inside HTML.

Examples:

- `{% for %}`
- `{% if %}`
- `{% url %}`
- `{% load static %}`

---

# Interview Tips

✅ Difference between `makemigrations` and `migrate` is one of the most frequently asked Django interview questions.

✅ `views.py` contains business logic, while `urls.py` handles routing.

✅ Context is the bridge between Python and HTML.

✅ Django stores applied migrations in the `django_migrations` table.
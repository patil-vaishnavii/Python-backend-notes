# Django Learning Notes

# 1. Django Project Settings (`settings.py`)

The `settings.py` file contains the configuration of the entire Django project.

Examples:
- Installed applications
- Database configuration
- Middleware
- Templates
- Static files
- Time zone
- Language

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
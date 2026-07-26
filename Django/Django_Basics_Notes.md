# Django Basics -- My Learning Notes

### Django Flow

``` text
Browser
    ↓
Project urls.py
    ↓
App urls.py
    ↓
views.py
    ↓
Template (HTML)
    ↓
Browser
```

# Purpose of Important Files

## 1. settings.py

Acts like the project's **configuration file**.

Responsibilities: 
- Registers installed apps 
- Database configuration 
- Template settings 
- Static files 
- Other project settings

Example:

``` python
INSTALLED_APPS = [
    "home",
]
```

Whenever I create a new app, I usually need to register it here.

------------------------------------------------------------------------

## 2. Project urls.py

Think of this as the **main traffic controller**.

It receives every request first and decides which app should handle it.

Example:

``` python
urlpatterns = [
    path("", include("home.urls")),
]
```

Meaning:

> "Send requests to the Home app."

------------------------------------------------------------------------

## 3. App urls.py

Handles routing **inside a specific app**.

Example:

``` python
urlpatterns = [
    path("", views.index),
]
```

Meaning:

> "Call the `index()` function."

------------------------------------------------------------------------

## 4. views.py

This is where the **actual work happens**.

A view: - Processes requests - Retrieves data - Returns HTML or other
responses

Example:

``` python
def index(request):
    return HttpResponse("Hello")
```

------------------------------------------------------------------------

# Complete Request Flow

``` text
User opens:

localhost:8000/

↓

Project urls.py

↓

App urls.py

↓

views.py

↓

Template (HTML)

↓

Response sent back to Browser
```

------------------------------------------------------------------------

# Why Two urls.py Files?

## Project urls.py

-   Knows about different apps.
-   Sends requests to the correct app.

## App urls.py

-   Knows the pages inside that app.
-   Connects URLs to views.

------------------------------------------------------------------------

# Why Do We Keep Updating These Files?

### When I create a new app

Update:

-   `settings.py`

------------------------------------------------------------------------

### When I create a new page

Update:

-   `urls.py`

------------------------------------------------------------------------

### When I write page logic

Update:

-   `views.py`

------------------------------------------------------------------------

# Checklist

Whenever you build something:

-   Created an app → Register it in `settings.py`
-   Created a page → Add a route in `urls.py`
-   Need functionality → Write it in `views.py`

------------------------------------------------------------------------

# Understanding Imports

Don't memorize imports.

Think of them as **connecting wires**.

``` python
from django.urls import path
from django.urls import include
from . import views
```

-   `path` → Creates URL routes.
-   `include` → Connects project URLs to app URLs.
-   `views` → Connects URLs to view functions.

------------------------------------------------------------------------

# Learning Roadmap

Master these steps before moving to advanced topics:

1.  Create a Django project.
2.  Create an app.
3.  Register the app in `settings.py`.
4.  Connect the app in the project's `urls.py`.
5.  Create routes in the app's `urls.py`.
6.  Write a view in `views.py`.
7.  Return an `HttpResponse`.
8.  Replace `HttpResponse` with an HTML template.

------------------------------------------------------------------------

# Key Takeaway

Don't memorize Django.

Understand the flow.

``` text
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




# Django Authentication Notes

## What is Authentication?

Authentication answers one question:

> **"Who is this user?"**

Authentication allows users to securely access parts of an application by verifying their identity.

Common authentication features include:

- ✅ Register (Sign Up)
- ✅ Login
- ✅ Logout

After a user logs in successfully, **Django remembers the user using sessions** so they don't need to log in again on every page.

---

# Django's Built-in Authentication System

One of Django's biggest advantages is that it already provides a complete authentication system.

You do **not** need to build everything from scratch.

Django already includes:

Yes, that's actually the approach used in many real Django projects.

Based on where you are now, here's the progression I'd recommend.

Your current project structure
```
FoodVerse/
│
├── restaurants/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── restaurant_list.html
│   │   └── restaurant_detail.html
│
├── FoodVerse/
│
└── manage.py
```
# creating another app accounts

Run:

python manage.py startapp accounts

Then add it to INSTALLED_APPS.

INSTALLED_APPS = [
    ...
    "restaurants",
    "accounts",
]

Why another app?

Because authentication is a completely different feature from restaurants.

Think of apps as modules.

```
restaurants
    ↓
Everything related to restaurants

accounts
    ↓
Everything related to users

orders
    ↓
Everything related to orders

payments
    ↓
Everything related to payments

```

This separation keeps the project organized and easier to maintain.

learn it in this order:

Phase 1 — User Model (Theory)

Understand:

***from django.contrib.auth.models import User***

Learn:

What is a User model?
What fields does it have?
How does Django store passwords?
Why use create_user() instead of create()?
How do we query users?
What is request.user?


Phase 2 — Registration

Create users.
```
Register
↓

User.objects.create_user()
↓

Saved in database
Phase 3 — Login
```
Understand:

authenticate()

and

login()

Phase 4 — Logout


logout(request)

Phase 5 — Protect pages

Use:

@login_required
Phase 6 — Show different navigation

For example:
```
Guest

Login
Register

becomes

Hello Vaishnavi

Dashboard
Logout
```
using

{% if user.is_authenticated %}
```
FoodVerse
│
├── restaurants
│      │
│      ├── Restaurant
│      ├── Menu
│      ├── Restaurant List
│      └── Restaurant Detail
│
├── accounts
│      │
│      ├── Register
│      ├── Login
│      ├── Logout
│      └── Profile
```
Later you can connect the two:
```
User
   │
   ├── Favorite Restaurants
   ├── Orders
   ├── Reviews
   └── Cart
```

suggested learning order
✅ Understand Django's built-in User model.
✅ Create the accounts app.
✅ Build registration.
✅ Build login.
✅ Build logout.
✅ Protect the profile/dashboard with login_required.
✅ Show different navigation for logged-in users.
✅ Connect users with restaurant features (favorites, reviews, orders, cart).

This order builds on what you already know and makes each new concept easier to understand.



# Django Authentication - Lesson 1: Understanding the User Model

Before we create login pages, we need to answer a simple question:

Where does Django store users?

The answer is:

Django already has a User model.

Think about your Restaurant model.

class Restaurant(models.Model):
    name = models.CharField(...)
    address = models.TextField()
    rating = models.DecimalField(...)

This creates a database table called  like:
```
id | name |	address	rating
```
Now imagine users.

Instead of creating this yourself:

class User(models.Model):
    username = ...
    password = ...
    email = ...

Django has already built it for you.

You simply import it:
```
from django.contrib.auth.models import User
```
What does the User model contain?

The User model already has many useful fields.

Some of the most important are:
```
Field	Purpose
username	User's unique username
email	Email address
password	Hashed password
first_name	First name
last_name	Last name
is_active	Whether the account can log in
is_staff	Can access the admin panel
is_superuser	Has all permissions
date_joined	Account creation date
last_login	Last login time
```

Notice something?

There is no plain-text password stored.

Where is it stored?

When you run migrations, Django creates a table named:

***auth_user***

If you open your database, you'll find something like:
```
id	| username|	email |	password
```
But the password won't look like this:

mypassword123

Instead, it looks something like:

pbkdf2_sha256$1000000$...

This is called a ***hashed password***.

***Why hash passwords?***

Imagine a website stored passwords like this:
```
Username	Password
vaishnavi	hello123
rahul	abc123
```
If someone stole the database, they would immediately know everyone's password.

***Instead, Django stores a hash:***
```
Username	Password
vaishnavi	pbkdf2_sha256$...
rahul	pbkdf2_sha256$...
```
A hash is a one-way transformation. Django can verify whether a password is correct, but it does not need to store the original password in plain text.

Creating a User

***Never do this:***
```
User.objects.create(
    username="vaishnavi",
    password="hello123"
)
```
***Why?***

Because it stores the ***password incorrectly (without hashing)***.

Instead, always use:
```
User.objects.create_user(
    username="vaishnavi",
    email="vaishnavi@gmail.com",
    password="hello123"
)
```
***create_user() automatically hashes the password before saving it.***

How does login work?

Suppose a user enters:
```
Username:
vaishnavi

Password:
hello123
```
Does Django compare:
```
hello123 == pbkdf2_sha256$...
```
No.

Instead:

- It takes the entered password (hello123).
- It hashes it using the same algorithm.
- It compares the new hash with the stored hash.
- If they match, authentication succeeds.
- The User model is just another model


For example:

from django.contrib.auth.models import User
```
users = User.objects.all()
```
Or fetch one user:
```
user = User.objects.get(username="vaishnavi")
```
Or filter:
```
users = User.objects.filter(is_staff=True)
```
The ORM works exactly the same way as with your Restaurant model.

Connecting this to FoodVerse

Right now, your project looks like this:

Restaurant
      │
      ├── Pizza Hut
      ├── KFC
      └── Domino's

Soon it will become:
```
User
   │
   ├── Username
   ├── Email
   └── Password (hashed)

Restaurant
   │
   ├── Pizza Hut
   ├── KFC
   └── Domino's
```
Later, you'll connect them:
```
User
   │
   ├── Favorite Restaurants
   ├── Orders
   ├── Reviews
   └── Cart
```
Before we write any authentication code

# Steps to create

Step 1: Create the accounts app

Run:

python manage.py startapp accounts
Step 2: Register it

In settings.py:

INSTALLED_APPS = [
    ...
    "restaurants",
    "accounts",
]


Quick Interview Questions

Try answering these yourself before looking up the answers:

Why doesn't Django require us to create a User model from scratch?
Why should you use create_user() instead of create()?
What is password hashing, and why is it important?
What database table stores Django's default users?
Can you query the User model using the Django ORM like your Restaurant model?

If you can answer these, you've understood the foundation.

Next Lesson

 Registration (Sign Up), You'll learn:

How to create a registration form.
How to validate user input.
How POST requests are used to create users.
How create_user() saves a new user securely.
How to redirect users after successful registration.

 build each file (urls.py, views.py, templates, and forms) together and explain every line.

- User model 
- Password hashing
- Login system
- Logout system
- Sessions
- Permissions

# Django Authentication Concepts

Django comes with a powerful built-in authentication system that handles most of the common tasks required for user management. Understanding these core concepts is essential before implementing authentication in any Django project.


# Creating the Project

Create a Django project and an app for authentication.

```bash
django-admin startproject myproject
cd myproject
python manage.py startapp accounts
```

Add the app inside `settings.py`.

```python
INSTALLED_APPS = [
    ...
    "accounts",
]
```

---

# Django User Model

Django already has a built-in **User** model.

Import it:

```python
from django.contrib.auth.models import User
```

The default User model contains fields such as:

- username
- password
- email
- first_name
- last_name

You do **not** need to create these fields yourself.

---

# User Registration (Sign Up)

When a user signs up, they typically provide:

```
Name
   ↓
Email
   ↓
Password
   ↓
Saved into Database
```

Create a new user using:

```python
from django.contrib.auth.models import User

User.objects.create_user(
    username="vaishnavi",
    email="abc@gmail.com",
    password="mypassword"
)
```

## Why use `create_user()`?

Always use:

```python
create_user()
```

❌ Do **not** use:

```python
create()
```

### Reason

`create_user()` automatically:

- Hashes the password
- Stores it securely
- Makes the account compatible with Django's authentication system

---

# Login

When a user enters:

- Username
- Password

Django checks whether the credentials are correct.

```python
from django.contrib.auth import authenticate

user = authenticate(
    username=username,
    password=password
)
```

If authentication succeeds:

```python
if user:
    print("Login successful")
```

Otherwise:

```python
print("Invalid credentials")
```

---

# Logging the User In

`authenticate()` only verifies the credentials.

To actually keep the user logged in, use:

```python
from django.contrib.auth import login

login(request, user)
```

After this:

- Django creates a session.
- The user stays logged in until they log out or the session expires.

---

# Logout

Logging out is simple.

```python
from django.contrib.auth import logout

logout(request)
```

This removes the user's session.

---

# Protecting Pages

Some pages should only be accessible to logged-in users.

Examples:

- `/profile`
- `/orders`
- `/dashboard`

Use the `login_required` decorator.

```python
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, "profile.html")
```

If the user is not logged in, Django automatically redirects them to the login page.

---

# Checking if a User is Logged In

Inside a view:

```python
if request.user.is_authenticated:
    print("Logged In")
else:
    print("Guest")
```

`is_authenticated` returns:

- `True` → User is logged in
- `False` → User is not logged in

---

# Accessing the Current User

The currently logged-in user is available through:

```python
request.user
```

Examples:

```python
request.user.username
```

```python
request.user.email
```

You can access any field stored in the User model.

---

# Authentication in Templates

Show different content depending on whether a user is logged in.

```django
{% if user.is_authenticated %}

Hello {{ user.username }}

<a href="">Logout</a>

{% else %}

<a href="">Login</a>

<a href="">Register</a>

{% endif %}
```

---

# Complete Authentication Flow

```text
Register
    ↓
User Created
    ↓
Login
    ↓
authenticate()
    ↓
login()
    ↓
Session Created
    ↓
User Visits Dashboard
    ↓
request.user
    ↓
Logout
    ↓
logout()
```

---

# Important Concepts to Master

- ✅ Django User Model
- ✅ `create_user()`
- ✅ `authenticate()`
- ✅ `login()`
- ✅ `logout()`
- ✅ `request.user`
- ✅ `is_authenticated`
- ✅ `login_required`
- ✅ Sessions
- ✅ Password Hashing (handled automatically by Django)

---

# Practice Project

1. Home
2. Register
3. Login
4. Dashboard (Only for logged-in users)
5. Logout

---

# Project Flow

```
Home
 │
 ├── Register
 │       │
 │       ▼
 │   User Created
 │
 ├── Login
 │       │
 │       ▼
 │ authenticate()
 │       │
 │       ▼
 │   login()
 │       │
 │       ▼
 │ Session Created
 │       │
 │       ▼
 └── Dashboard
         │
         ▼
      Logout
         │
         ▼
    Session Removed
```

---

# Quick Revision

| Function / Feature | Purpose |
|--------------------|---------|
| `User` | Django's built-in user model |
| `create_user()` | Creates a new user and hashes the password |
| `authenticate()` | Verifies username and password |
| `login()` | Creates a session and logs the user in |
| `logout()` | Ends the user's session |
| `request.user` | Returns the current logged-in user |
| `is_authenticated` | Checks whether a user is logged in |
| `login_required` | Restricts access to authenticated users |

---

# Key Takeaways

- Django provides a powerful built-in authentication system.
- Never store passwords manually—use `create_user()`.
- `authenticate()` verifies credentials.
- `login()` creates the user's session.
- `logout()` removes the session.
- Use `login_required` to protect sensitive pages.
- Access the current user through `request.user`.
- Display different UI in templates using `user.is_authenticated`.

---


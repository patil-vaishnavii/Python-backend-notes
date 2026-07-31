# Django Forms

## What is a Django Form?

A Django Form is a Python class that helps us:

- Generate HTML forms
- Validate user input
- Display validation errors
- Clean form data
- Save data to the database (when using ModelForm)

Instead of manually handling HTML inputs and validation, Django provides a structured way to work with forms.

---

# HTML Form vs Django Form

## HTML Form

Example:

```html
<form method="POST">
    <input type="text" name="username">
    <input type="password" name="password">
</form>
```

When this form is submitted, the developer must:

- Read every input from `request.POST`
- Validate every field
- Check if passwords match
- Display errors
- Save the data

Everything is written manually.

---

## Django Form

Django says:

> "I'll handle most of that work for you."

A Django Form:

- Generates HTML
- Validates input
- Displays errors automatically
- Cleans data
- Can save data

This reduces code and improves security.

---

# Types of Django Forms

There are two main types.

## 1. forms.Form

Used when the data is **not connected to a database model**.

Example:

Contact Us Form

- Name
- Email
- Message

Since there is no database table, we use:

```python
from django import forms

class ContactForm(forms.Form):
    ...
```

---

## 2. forms.ModelForm

Used when the form is connected to a Django model.

Example:

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
```

Instead of creating every field manually, Django creates them from the model.

```python
class BookForm(forms.ModelForm):
    ...
```

ModelForm is commonly used for CRUD operations.

---

# What is UserCreationForm?

`UserCreationForm` is a **built-in Django form**.

It is provided by Django for user registration.

Import:

```python
from django.contrib.auth.forms import UserCreationForm
```

It already contains:

- Username
- Password
- Password Confirmation

It also automatically performs validation:

- Username already exists
- Passwords match
- Password follows Django's password rules

Instead of writing all of this ourselves, we reuse Django's built-in form.

---

# Understanding RegistrationForm

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
```

---

## Line-by-Line Explanation

### Import UserCreationForm

```python
from django.contrib.auth.forms import UserCreationForm
```

Imports Django's ready-made registration form.

---

### Import User Model

```python
from django.contrib.auth.models import User
```

Imports Django's built-in User model.

Django already provides the User table.

There is no need to create our own user model for basic authentication.

---

### Inheritance

```python
class RegistrationForm(UserCreationForm):
```

This is inheritance.

Meaning:

> Create a new form based on Django's existing UserCreationForm.

We inherit all the functionality and customize only what we need.

---

### Meta Class

```python
class Meta:
```

The Meta class provides configuration for the form.

It tells Django:

- Which model this form is connected to
- Which fields should appear

---

### Model

```python
model = User
```

This form works with the Django User model.

When we call:

```python
form.save()
```

A new record is inserted into Django's `auth_user` table.

---

### Fields

```python
fields = [
    "username",
    "email",
    "password1",
    "password2",
]
```

These are the fields Django should generate.

Instead of writing HTML manually, Django creates these inputs automatically.

---

# How the HTML is Generated

Template:

```html
<form method="POST">

    {% csrf_token %}

    {{ form.as_p }}

    <button type="submit">
        Register
    </button>

</form>
```

`{{ form.as_p }}` automatically generates HTML like:

```html
<p>
    Username:
    <input ...>
</p>

<p>
    Email:
    <input ...>
</p>

<p>
    Password:
    <input ...>
</p>

<p>
    Confirm Password:
    <input ...>
</p>
```

---

# Complete Flow

```
RegistrationForm
        │
        ▼
UserCreationForm
        │
        ▼
User Model
        │
        ▼
auth_user Table
        │
        ▼
Database
```

---

# Why Use Django Forms?

Without Django Forms:

```python
username = request.POST["username"]
password = request.POST["password"]
confirm = request.POST["confirm"]

if password != confirm:
    ...

if len(password) < 8:
    ...

...
```

The developer writes all validation manually.

With Django Forms:

```python
if form.is_valid():
    form.save()
```

Django handles:

- Validation
- Error messages
- Password hashing
- Saving the user

---

# Forms Used in This Project

## Registration

```python
UserCreationForm
```

Purpose:

Create a new user account.

---

## Login

```python
AuthenticationForm
```

Purpose:

Authenticate an existing user.

---

## Add Book

```python
BookForm(ModelForm)
```

Purpose:

Create a new book.

---

## Edit Book

```python
BookForm(ModelForm)
```

Purpose:

Update an existing book.

---

# Interview Questions

## Q1. What is a Django Form?

A Django Form is a Python class that helps generate HTML forms, validate user input, display errors, clean data, and save information securely.

---

## Q2. What is the difference between Form and ModelForm?

**Form**

- Not connected to a database model.
- Used for forms like Contact Us, Feedback, Search, etc.

**ModelForm**

- Connected to a Django model.
- Automatically generates fields from the model.
- Used for CRUD operations.

---

## Q3. Why do we use UserCreationForm?

Because Django already provides:

- Username validation
- Password validation
- Password confirmation
- Password hashing
- User creation

This saves development time and follows Django's security best practices.

---

## Q4. What does `form.is_valid()` do?

It validates all form fields.

If every field passes validation, it returns `True`.

Otherwise, it returns `False` and stores the validation errors.

---

## Q5. What does `form.save()` do?

It saves the validated data into the associated database model.

For `UserCreationForm`, it creates a new user in the `auth_user` table and stores the password in hashed form.

---

# Key Takeaways

- Django Forms reduce manual coding.
- `Form` is used when there is no database model.
- `ModelForm` is used for CRUD operations.
- `UserCreationForm` is Django's built-in registration form.
- `AuthenticationForm` is Django's built-in login form.
- `form.is_valid()` performs validation.
- `form.save()` saves validated data to the database.
- Django automatically hashes passwords before storing them.
# Step 1: Understand the built-in User model

answer this question:

Where will user information be stored?

Django  provides a complete ***User model***.

It contains fields like:
```
id
username
first_name
last_name
email
password
is_staff
is_superuser
is_active
last_login
date_joined
```

There is a password field, but Django never stores the actual password.

Instead, it stores a hashed version.

Example:

User enters:
```
Password = food123
```
Database stores something like:
```
pbkdf2_sha256$1000000$...
```
Even the database administrator cannot recover the original password.

This is one of the ***biggest security features of Django***.

# Step 2: Why use UserCreationForm?
Imagine you create your own HTML form.

Someone enters:
```
Username : vaishnavi
Password : abc123
Confirm Password : xyz123
```
If you save this directly, you'll create a broken account.

You would need to manually check:

Is the username already taken?
Are both passwords the same?
Is the password strong enough?
Hash the password before saving.

Django already solves all of this.

That's why we use UserCreationForm.

It automatically:

✅ Validates the username

✅ Checks password strength

✅ Confirms both passwords match

✅ Hashes the password

✅ Saves the user correctly


# Validation

form.is_valid()

Django checks everything automatically:

✔ username already exists?

✔ passwords match?

✔ password strong enough?

✔ required fields filled?

You didn't write any validation code—that's the power of UserCreationForm.

# Saving

form.save()

This creates a new row in Django's auth_user table.

It also hashes the password before saving it.

# {{ form.as_p }}

This single line tells Django:

"Take my RegisterForm object and generate the HTML automatically."

This is an important Django concept

There are two ways to display forms.

# Method 1 (Learning / Quick)
{{ form.as_p }}

✅ Fast

❌ Very little control over the appearance.

## Method 2 (Professional)
{{ form.username }}
{{ form.email }}
{{ form.password1 }}
{{ form.password2 }}

✅ Complete control over the UI.

✅ Used in real projects.

# Authentication System
```
Click SIGN UP
        │
        ▼
register URL
        │
        ▼
register_view()
        │
        ▼
RegisterForm
        │
        ▼
UserCreationForm
        │
        ▼
Validation
        │
        ▼
Password Hashing
        │
        ▼
User model
        │
        ▼
auth_user table
```

# Authentication Form
AuthenticationForm

Displays the login form and performs basic validation (required fields, etc.).

authenticate()

Checks the credentials against the users stored in Django's auth_user table.

Conceptually:
```
Username: vaishnavi
Password: Foodverse@123
        │
        ▼
auth_user table
        │
        ▼
Password hash comparison
        │
        ▼
Returns User object OR None
```
It does not log the user in. It only checks if the credentials are valid.

ogin()

If authenticate() returns a valid user, login() creates a session.

A session is Django's way of remembering:

"This browser belongs to this logged-in user."

Without a session, the user would have to log in again every time they opened a new page.
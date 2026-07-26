# Creating a Project

## Step 1: Create a project folder
- mkdir myproject
- cd myproject

## Step 2: Create a virtual enviroment
- python -m venv venv

## Step 3: Activate the virtual environment
- venv\Scripts\activate

When activated , the terminal will show something like:
(venv)C:\Users\YourName\myproject>

## Step 4: Install Django
pip install django

## Step 5: Check Django Version
django-admin --version

## Step 6: Create the Django project
django-admin startproject config .

- config is the project name. The . tells Django to create the project in the current folder.

## Step 7: Run the Server
python manage.py runserver

click on the provided path
If you see "The install worked successfully!",your project is set up correctly.

## Step 8: Create an app

python manage.py startapp blog

-You can replace blog with any app name, such as accounts, students,products etc.


## Commands to remember 

mkdir myproject
cd myproject

python -m venv venv
venv\Scripts\activate

pip install django

django-admin startproject config .

python manage.py runserver

python manage.py startapp blog

python manage.py makemigrations 
python manage.py migrate

python manage.py createsuperuser




Perfect! 🎉 **Django has been installed successfully.**

Let's go through the output so you understand what each line means.

```text
Installing wheels...
```

A **wheel** is a pre-built Python package. Instead of downloading the source code and compiling it, `uv` downloads a ready-to-use package, which makes installation much faster.

---

### This warning:

```text
warning: Failed to hardlink files; falling back to full copy.
```

**Don't worry about it. It's not an error.**

It simply means:

* `uv` tried to create a **hard link** (a fast way to copy files).
* Windows couldn't do it (often because the cache and project are on different drives or due to Windows filesystem limitations).
* So `uv` used a normal file copy instead.

Your installation **completed successfully**, so you can safely ignore this warning.

---

### Installed packages

```text
+ asgiref==3.12.1
+ django==6.0.7
+ sqlparse==0.5.5
```

These are the packages Django needs.

* **django** → The Django framework itself.
* **asgiref** → Helps Django handle asynchronous requests (ASGI).
* **sqlparse** → Lets Django format and analyze SQL queries.

You didn't install `asgiref` or `sqlparse` manually—`uv` installed them automatically because Django depends on them.

---

# Now you're ready to create your Django project.

Since you're already inside:

```text
D:\MyProjects\First-Django-Project
```

run:

```powershell
django-admin startproject config .
```

Notice the **`.` (dot)** at the end.

It means:

> "Create the Django project in the current folder."

After that, your folder should look like this:

```text
First-Django-Project
│
├── .venv
├── manage.py
├── config
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
```

# Features
1. Very fast
2. Reasssuringly secure.
3. Exceedingly scalable.

Why not install Django once globally?

Imagine you installed Django globally.

Now:

Project A needs Django 4.2
Project B needs Django 5.2

If you upgrade the global installation to 5.2:

Project A ❌ May stop working
Project B ✅ Works

That's why professionals avoid relying on globally installed packages.
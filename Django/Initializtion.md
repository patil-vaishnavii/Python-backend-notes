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


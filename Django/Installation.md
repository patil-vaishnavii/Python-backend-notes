1. Install Python.


# Virtual Environment

Two ways to create a virtual environment

## Method 1 (Recommended for Python 3.3+)

Use the built-in venv module:

>>python -m venv venv

- Comes with Python (no extra installation needed).
- This is the modern, recommended approch.
- Most Django projects today use this.

## Method 2(Older but still valid)

Install Virtual Environment.

>> pip install virtualenv

In virtual environment , we install all the required packages to build the project.
It's a kind of room,space in which we install only those dependencies which are required to complete any particular project.

Then create a virtual environment:

virtualenv venv

Here:
- pip install virtualenv installs a third-party tool called virtualenv.
- virtualenv venv creates a virtual environment named venv.






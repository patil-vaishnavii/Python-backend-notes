## A virtual environment is active only in the terminal where you activated it.

Absolutely! Here are **simple beginner-friendly notes** based on everything we've learned today.

---

# 📘 Virtual Environment (venv / .venv) Notes

## What is a Virtual Environment?

A **Virtual Environment (venv)** is an **isolated Python environment** created for a specific project.

It keeps each project's Python packages separate from other projects.

---

# Why do we use a Virtual Environment?

Suppose you have two projects:

### Project A

* Django 4.2

### Project B

* Django 6.0

If you install Django globally, both projects will use the same version, which can cause conflicts.

With a virtual environment:

```text
Project A
│
└── .venv
      └── Django 4.2

Project B
│
└── .venv
      └── Django 6.0
```

Each project has its own packages.

---

# One Project = One Virtual Environment

**Rule to remember**

```text
1 Project
       ↓
1 Virtual Environment
       ↓
1 Independent Set of Packages
```

---

# Why not install Django globally?

Without a virtual environment:

```text
Global Python
│
└── Django 4.2
```

Later you upgrade:

```text
pip install --upgrade django
```

Now:

```text
Global Python
│
└── Django 6.0
```

Older projects may stop working.

Virtual environments prevent this problem.

---

# Creating a Virtual Environment (using uv)

```powershell
uv venv
```

This creates

```text
.venv/
```

---

# Why is it called `.venv`?

The `.` simply makes it a hidden folder (common convention).

Both are correct:

```text
venv
```

or

```text
.venv
```

Most modern projects use:

```text
.venv
```

---

# Activating the Virtual Environment

### Windows PowerShell

```powershell
.\.venv\Scripts\activate
```

or

```powershell
.\.venv\Scripts\activate.ps1
```

---

### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

---

### Linux/macOS

```bash
source .venv/bin/activate
```

---

# How do I know it is activated?

Your terminal changes from

```text
PS D:\Project>
```

to

```text
(ProjectName) PS D:\Project>
```

That means you're using the project's Python.

---

# Do I need to activate it every time?

**Yes.**

Every new terminal starts with the global Python.

Whenever you open a new terminal:

1. Open the project folder.
2. Activate the virtual environment.

---

# If I close PowerShell?

Closing the terminal **deactivates** the virtual environment.

Next time:

```powershell
.\.venv\Scripts\activate
```

again.

---

# Does VS Code activate it automatically?

Usually **Yes**.

If VS Code detects `.venv`, opening a new terminal often activates it automatically.

If not:

* Press **Ctrl + Shift + P**
* Choose **Python: Select Interpreter**
* Select

```text
.venv\Scripts\python.exe
```

---

# Do I install Django every time?

No.

You install Django **once per virtual environment**.

Example:

```powershell
uv pip install django
```

After that, Django stays inside `.venv`.

You only install it again when creating a **new project** (new virtual environment).

---

# Typical Django Project Setup

```powershell
mkdir MyProject

cd MyProject

uv venv

.\.venv\Scripts\activate

uv pip install django

django-admin startproject config .
```

---

# Folder Structure

```text
MyProject
│
├── .venv
│
├── manage.py
│
└── config
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    ├── wsgi.py
```

### Remember these 5 points:

✅ A virtual environment isolates project packages.

✅ Every project should have its own `.venv`.

✅ Activate the virtual environment before running Django commands.

✅ Closing the terminal deactivates the virtual environment.

✅ Install Django once inside each project's virtual environment.

---


> **"Why do we use a virtual environment in Python?"**

> "A virtual environment creates an isolated Python environment for each project. It allows every project to have its own dependencies and package versions, preventing conflicts between projects. For example, one project can use Django 4.2 while another uses Django 6.0 without affecting each other."

## why used uv?
fast and popular.
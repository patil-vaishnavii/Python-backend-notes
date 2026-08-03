# Django Database Tables — Complete Field-by-Field Breakdown

This document provides a field-by-field breakdown of the database tables in the exact viewer sequence. It includes their fields, system importance, real-world utility, and the Django package or built-in application responsible for creating them.

---

## 1. `auth_group`

### Fields

* `id` — Integer: Auto-incrementing primary key.
* `name` — Varchar: Unique group/role name.

### Importance

**High** — Groups users into structural cohorts for clean, sweeping permission changes.

### Use

Creating system-wide roles such as:

* Moderator
* Editor
* Admin

### Package / App Group

Created by `django.contrib.auth` through its internal initial migrations.

---

## 2. `auth_group_permissions`

### Fields

* `id` — Integer: Auto-incrementing primary key.
* `group_id` — Foreign Key → `auth_group`: The target user group.
* `permission_id` — Foreign Key → `auth_permission`: The target permission.

### Importance

**High** — A junction table that determines exactly what features an entire user group can modify.

### Use

For example, mapping a **Moderator** group to a permission such as:

> Can delete task

### Package / App Group

Created by `django.contrib.auth`.

---

## 3. `auth_permission`

### Fields

* `id` — Integer: Auto-incrementing primary key.
* `name` — Varchar: Human-readable permission string, such as `"Can add task"`.
* `content_type_id` — Foreign Key → `django_content_type`: The target model the permission applies to.
* `codename` — Varchar: Machine-readable lookup code, such as `"add_task"`.

### Importance

**High** — Represents Django's granular permission and authorization system.

### Use

Permissions can be checked dynamically using rules such as:

```python
@permission_required('todo.add_task')
```

### Package / App Group

Created by `django.contrib.auth`.

---

## 4. `auth_user`

### Fields

* `id` — Integer: Auto-incrementing primary key.
* `password` — Varchar: Securely hashed password.
* `last_login` — Datetime: Timestamp documenting the user's latest login.
* `is_superuser` — Boolean: Global permission override flag.
* `username` — Varchar: Unique identifier used to sign into the application.
* `first_name` — Varchar: Optional first name.
* `last_name` — Varchar: Optional last name.
* `email` — Varchar: User's email address.
* `is_staff` — Boolean: Controls access to the Django administration site.
* `is_active` — Boolean: Determines whether the account is active and allowed to authenticate.
* `date_joined` — Datetime: Timestamp recording when the account was created.

### Importance

**Critical** — The core authentication table that stores user identity and account information.

### Use

Handles:

* User authentication
* User account information
* Password storage
* User status
* Staff status
* Superuser status
* Login tracking

### Package / App Group

Created by `django.contrib.auth`.

---

## 5. `auth_user_groups`

### Fields

* `id` — Integer: Auto-incrementing primary key.
* `user_id` — Foreign Key → `auth_user`: Target user account.
* `group_id` — Foreign Key → `auth_group`: Target user group.

### Importance

**Medium-High** — Manages the Many-to-Many relationship between users and groups.

### Use

For example:

> User ID 5 belongs to Group ID 2.

This allows users to inherit permissions from their assigned groups.

### Package / App Group

Created by `django.contrib.auth`.

---

## 6. `auth_user_user_permissions`

### Fields

* `id` — Integer: Auto-incrementing primary key.
* `user_id` — Foreign Key → `auth_user`: Target user profile.
* `permission_id` — Foreign Key → `auth_permission`: Permission assigned to the user.

### Importance

**Medium** — Used for assigning individual permissions directly to a specific user.

### Use

For example, a specific user can be given permission to edit system data without giving that permission to every user in their group.

### Package / App Group

Created by `django.contrib.auth`.

---

## 7. `django_admin_log`

### Fields

* `id` — Integer: Auto-incrementing primary key.
* `action_time` — Datetime: Timestamp recording when the action occurred.
* `object_id` — Text: Primary key of the modified object.
* `object_repr` — Varchar: Text representation of the modified object, usually generated using the model's `__str__()` method.
* `action_flag` — Small Integer:

  * `1` = Creation
  * `2` = Modification
  * `3` = Deletion
* `change_message` — Text: Description of the changes made.
* `content_type_id` — Foreign Key → `django_content_type`: Identifies the model that was modified.
* `user_id` — Foreign Key → `auth_user`: Identifies the administrator who performed the action.

### Importance

**Medium** — Provides audit and activity tracking for Django Admin.

### Use

Allows you to investigate:

* Who changed data
* When the change happened
* What object was changed
* Whether it was created, modified, or deleted

### Package / App Group

Created by `django.contrib.admin`.

> **Note:** `django.contrib.admin` relies heavily on Django's authentication system, so `django.contrib.auth` is also involved in the admin functionality.

---

## 8. `django_content_type`

### Fields

* `id` — Integer: Auto-incrementing primary key.
* `app_label` — Varchar: Name of the Django application, such as `"todo"`.
* `model` — Varchar: Lowercase name of the model, such as `"task"`.

### Importance

**Very High** — Maintains a registry of the models installed in a Django project.

### Use

It allows Django to refer to models dynamically.

For example:

```text
app_label = todo
model = task
```

Django can use this information for features such as:

* Permissions
* Generic relationships
* Admin functionality

### Package / App Group

Created by `django.contrib.contenttypes`.

---

## 9. `django_migrations`

### Fields

* `id` — Integer: Auto-incrementing primary key.
* `app` — Varchar: Name of the Django application associated with the migration.
* `name` — Varchar: Name of the migration file, such as `"0001_initial"`.
* `applied` — Datetime: Date and time when the migration was applied.

### Importance

**Critical** — Keeps track of which migrations have already been applied to the database.

### Use

When you run:

```bash
python manage.py migrate
```

Django checks this table to determine:

1. Which migrations have already been applied.
2. Which migrations are still pending.
3. Which database changes need to be performed.

This prevents Django from repeatedly applying the same migration.

### Package / App Group

**Core Django migration system.**

This table is created as part of Django's migration infrastructure and is used to track migrations for all installed applications.

---

## 10. `django_session`

### Fields

* `session_key` — Varchar: Unique identifier for a user's session.
* `session_data` — Text: Encoded/serialized data associated with the session.
* `expire_date` — Datetime: Date and time when the session expires.

### Importance

**Critical** — Provides session management for Django applications.

### Use

Sessions allow Django to remember information between HTTP requests.

For example:

* Keeping a user logged in
* Remembering temporary user data
* Maintaining shopping carts
* Storing multi-step form information

When a user logs in, Django can use the session to remember that the user is authenticated while navigating between pages.

### Package / App Group

Created by:

```python
django.contrib.sessions
```

---

## 11. `sqlite_sequence`

### Fields

* `name` — Text: Name of the table whose automatically generated IDs are being tracked.
* `seq` — Integer: Highest value assigned by SQLite's `AUTOINCREMENT` mechanism.

### Importance

**Low-Medium** — An internal SQLite database management table.

### Use

It is created and managed by the SQLite database engine rather than Django.

It helps SQLite keep track of automatically generated integer IDs for tables using the relevant `AUTOINCREMENT` mechanism.

### Package / App Group

**SQLite Database Internal**

This is not a Django-created application table. It is automatically maintained by SQLite when required.

---

## 12. `todo_task`

### Fields

* `id` — Integer: System-generated primary key.
* Custom fields — These are the fields explicitly defined in your Django model.

For example:

```python
title = models.CharField(...)
description = models.TextField(...)
is_completed = models.BooleanField(...)
```

The exact fields depend on the `Task` model defined in your application.

### Importance

**Maximum** — This is your application's actual domain-data table.

### Use

Stores the actual task information created through your ToDo application.

For example:

```text
Task 1 → Complete Django project
Task 2 → Study migrations
Task 3 → Push project to GitHub
```

### Package / App Group

Created by your custom Django application:

```text
todo
```

The table name follows Django's default naming convention:

```text
<app_name>_<model_name>
```

Therefore:

```text
todo_task
```

means:

```text
App       → todo
Model     → Task
Table     → todo_task
```

---

# Quick Summary

| Table                        | Main Purpose                               | Created By                    |
| ---------------------------- | ------------------------------------------ | ----------------------------- |
| `auth_group`                 | Stores user groups                         | `django.contrib.auth`         |
| `auth_group_permissions`     | Connects groups with permissions           | `django.contrib.auth`         |
| `auth_permission`            | Stores available permissions               | `django.contrib.auth`         |
| `auth_user`                  | Stores user accounts                       | `django.contrib.auth`         |
| `auth_user_groups`           | Connects users with groups                 | `django.contrib.auth`         |
| `auth_user_user_permissions` | Connects users with individual permissions | `django.contrib.auth`         |
| `django_admin_log`           | Tracks Django Admin actions                | `django.contrib.admin`        |
| `django_content_type`        | Registry of installed models               | `django.contrib.contenttypes` |
| `django_migrations`          | Tracks applied migrations                  | Django migration system       |
| `django_session`             | Stores session information                 | `django.contrib.sessions`     |
| `sqlite_sequence`            | SQLite internal sequence tracking          | SQLite                        |
| `todo_task`                  | Stores your application's tasks            | Your `todo` app               |

---

# Important Concept

The tables can broadly be divided into three categories:

### 1. Django Authentication & Authorization Tables

```text
auth_user
auth_group
auth_permission
auth_user_groups
auth_user_user_permissions
auth_group_permissions
```

These handle **users, groups, and permissions**.

### 2. Django System Tables

```text
django_admin_log
django_content_type
django_migrations
django_session
```

These support Django's built-in framework functionality.

### 3. Database / Application Tables

```text
sqlite_sequence
todo_task
```

* `sqlite_sequence` → Internal SQLite functionality.
* `todo_task` → Your actual application's business data.

---

# Key Takeaway

The most important distinction is:

```text
Django's built-in tables
        ↓
Support Django features
        ↓
Authentication
Authorization
Sessions
Admin
Migrations
Content Types

Your custom table
        ↓
todo_task
        ↓
Stores your application's actual Task data
```

So, when you look at your database, **not every table represents something you explicitly created**. Many tables are automatically generated by Django's built-in applications when you run migrations.

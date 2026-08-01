# Django Database and Migrations

## 1. Before `migrate`, is the database empty?

If a Django project has been created but migrations have not been applied, the SQLite database may exist, but the required Django database tables have not necessarily been created.

Django comes with built-in applications:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

These built-in applications already contain migration files supplied by Django.

For example:

```text
django.contrib.auth
        ↓
Django already has migration files
        ↓
python manage.py migrate
        ↓
Auth-related database tables are created
```

Therefore, we can run:

```powershell
python manage.py migrate
```

without running `makemigrations` first.

Django uses the migration files that already exist for its built-in applications.

---

# 2. Why do we need `makemigrations`?

We need `makemigrations` when we create or modify our own models.

For example:

```python
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

Django detects that we have created a new model, but it does not immediately modify the database.

We run:

```powershell
python manage.py makemigrations
```

Django creates a migration file:

```text
notes/
└── migrations/
    └── 0001_initial.py
```

The migration file contains instructions for changing the database.

Then we run:

```powershell
python manage.py migrate
```

Django applies those instructions to the database.

The process is:

```text
models.py
   ↓
makemigrations
   ↓
migration file
   ↓
migrate
   ↓
database
```

### Key difference

**`makemigrations` → creates migration instructions**

**`migrate` → applies migration instructions to the database**

---

# 3. Why did `migrate` work without `makemigrations`?

Nothing is wrong with the project.

Django's built-in applications already have migration files.

For example:

```text
Django
  │
  ├── auth migrations
  ├── session migrations
  ├── admin migrations
  └── contenttypes migrations
          ↓
       migrate
          ↓
       Database
```

Running:

```powershell
python manage.py migrate
```

can create tables such as:

```text
django_session
auth_user
django_admin_log
django_content_type
```

The `django_session` table that was missing earlier was one of the tables created by Django's existing session migrations.

---

# 4. What happens when we create the `Note` model?

Suppose we create:

```python
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

Run:

```powershell
python manage.py makemigrations
```

Django generates something similar to:

```text
notes/migrations/0001_initial.py
```

Then run:

```powershell
python manage.py migrate
```

Django creates the new `notes_note` table.

The database may now contain:

```text
django_session
auth_user
django_admin_log
django_content_type
...
notes_note
```

The new migration does not recreate the existing Django tables from scratch.

Django tracks which migrations have already been applied.

---

# 5. What happens when we change a model later?

Suppose the original model is:

```python
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

Later, we add:

```python
updated_at = models.DateTimeField(auto_now=True)
```

Run:

```powershell
python manage.py makemigrations
```

Django may create:

```text
0002_note_updated_at.py
```

Then:

```powershell
python manage.py migrate
```

The database structure changes from:

```text
notes_note
├── id
├── title
└── content
```

to:

```text
notes_note
├── id
├── title
├── content
└── updated_at
```

The previous migration remains:

```text
0001_initial.py
```

The new migration records the next change:

```text
0002_note_updated_at.py
```

Migration files therefore form a **history of database changes**.

---

# 6. What happens if migration files are deleted?

There are two important situations.

## Situation A — Migration has not been applied

Suppose:

```text
models.py
    ↓
makemigrations
    ↓
0001_initial.py
```

but:

```powershell
python manage.py migrate
```

has not been run yet.

In a local development project, deleting that migration can generally be recovered by creating a new migration:

```powershell
python manage.py makemigrations
```

This is because the database has not been changed by that migration.

---

# 7. Situation B — Migration has already been applied

Suppose:

```text
models.py
    ↓
0001_initial.py
    ↓
migrate
    ↓
DATABASE CHANGED
```

Now the migration has already been applied.

If we delete:

```text
0001_initial.py
```

the database may still contain:

```text
notes_note
```

Django also keeps track of applied migrations in a database table called:

```text
django_migrations
```

It may contain:

```text
notes | 0001_initial
```

The situation could therefore become:

```text
Migration files:
    0001_initial.py → deleted

Database:
    notes_note table → exists

django_migrations:
    notes | 0001_initial → marked as applied
```

The migration history and migration files are now inconsistent.

### Rule

Do not casually delete migration files that have already been applied.

This is particularly important when:

* the project is shared
* migrations have been pushed to GitHub
* the project is deployed
* the database contains important data
* multiple developers work on the project

---

# 8. What if we delete the database and migrations?

Some tutorials use the following approach:

```text
db.sqlite3                  ← delete
notes/migrations/0001...    ← delete
```

Then recreate the migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

This can be appropriate for a small personal development project when intentionally resetting everything.

It essentially means:

> Start the database and migration history from the beginning.

However, this should not be the default solution for migration errors.

Avoid doing this when:

* the project is deployed
* other developers use the project
* the database contains important data
* migrations have already been shared
* real user data exists

---

# 9. What happens when we add a field to an existing model?

Suppose the database already contains:

```text
Note 1 → Django Notes
Note 2 → Python Notes
```

Then we add a new field:

```python
created_at = models.DateTimeField(...)
```

Django has to determine what value existing records should receive.

The situation is:

```text
Existing data
      ↓
New required field
      ↓
"What value should existing records receive?"
```

Therefore, `makemigrations` may ask for a default value.

Always read migration prompts carefully instead of automatically accepting an option without understanding it.

---

# 10. Recommended migration workflow

Whenever a model is created or changed:

### Step 1 — Modify `models.py`

```python
class Note(models.Model):
    ...
```

### Step 2 — Create migration instructions

```powershell
python manage.py makemigrations
```

### Step 3 — Apply the migrations

```powershell
python manage.py migrate
```

### Step 4 — Check migration status if needed

```powershell
python manage.py showmigrations
```

---

# 11. What should be done?

### Do:

* Change models normally.
* Run `makemigrations` after model changes.
* Run `migrate` after creating migrations.
* Commit migration files to Git.
* Read migration prompts carefully.
* Keep migration history consistent.
* Understand migration errors before making changes.

---

# 12. What should not be done?

### Do not:

* Delete applied migration files casually.
* Delete `db.sqlite3` as the first response to a migration error.
* Manually modify database tables when Django migrations can handle the change.
* Forget to run `migrate`.
* Assume `makemigrations` has already changed the database.
* Ignore migration files when committing the project to Git.
* Repeatedly run `makemigrations` without checking what Django is reporting.

---

# 13. The Golden Rule

Whenever you change a model:

```text
                 CHANGE MODEL
                      ↓
            python manage.py
             makemigrations
                      ↓
             Migration created
                      ↓
            python manage.py
                migrate
                      ↓
             Database updated
```

The overall direction is:

```text
models.py
    ↓
migration files
    ↓
database
```

Do not think of the process as:

```text
models.py → database directly
```

The **migration files are the bridge between Django models and the database**.

---

# 14. NotesApp Example

For the NotesApp, Django's built-in migrations have already been applied:

```powershell
python manage.py migrate
```

Therefore, Django's built-in tables such as the session and authentication tables now exist.

The `Note` model has not yet been finalized because each note needs to belong to the logged-in user.

The model will eventually be similar to:

```python
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

Then:

```powershell
python manage.py makemigrations
python manage.py migrate
```

will create the Notes database structure.

It will not destroy or recreate the existing Django authentication and session tables.

---

# Quick Revision

```text
MODEL
  ↓
makemigrations
  ↓
MIGRATION FILE
  ↓
migrate
  ↓
DATABASE
```

### Remember:

**Models describe what we want.**

**Migrations record the database changes.**

**The database stores the result.**

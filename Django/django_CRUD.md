# NotesApp — CRUD Implementation Flow

## 1. CREATE — Create a Note

| File                                     | Action                                                               |
| ---------------------------------------- | -------------------------------------------------------------------- |
| `notes/models.py`                        | Created the `Note` model with `user`, `title`, and `content`.        |
| `notes/migrations/0001_initial.py`       | Migration created for the `Note` model.                              |
| `notes/admin.py`                         | Registered `Note` for admin/testing purposes.                        |
| `notes/views.py`                         | Created `create_note()` view to receive form data and create a note. |
| `notes/urls.py`                          | Added `/create/` URL for `create_note`.                              |
| `notes/templates/notes/create_note.html` | Created HTML form for title and content.                             |
| `notes/templates/notes/home.html`        | Added `Create Note` link and displayed created notes.                |

### Create Flow

```text
User
  ↓
Create Note page
  ↓
Enter title + content
  ↓
Submit POST request
  ↓
create_note()
  ↓
request.POST
  ↓
Get title + content
  ↓
request.user
  ↓
Note.objects.create()
  ↓
Database
  ↓
redirect("home")
  ↓
Home displays note
```

---

# 2. READ — Display Notes

| File                              | Action                                                                   |
| --------------------------------- | ------------------------------------------------------------------------ |
| `notes/views.py`                  | Created `home()` view to retrieve notes belonging to the logged-in user. |
| `notes/urls.py`                   | Added `/` URL for `home`.                                                |
| `notes/templates/notes/home.html` | Used `for` loop to display notes.                                        |

### Read Flow

```text
User logs in
  ↓
Visits Home /
  ↓
home()
  ↓
request.user
  ↓
Note.objects.filter(user=request.user)
  ↓
Notes retrieved from database
  ↓
notes passed to template
  ↓
home.html
  ↓
{% for note in notes %}
  ↓
Notes displayed as cards/content
```

---

# 3. UPDATE — Edit a Note

| File                                   | Action                                                             |
| -------------------------------------- | ------------------------------------------------------------------ |
| `notes/views.py`                       | Created `edit_note()` view to retrieve and update the user's note. |
| `notes/urls.py`                        | Added `/edit/<int:id>/` URL.                                       |
| `notes/templates/notes/edit_note.html` | Created form with existing title and content.                      |
| `notes/templates/notes/home.html`      | Added `Edit` button/link to each note.                             |

### Update Flow

```text
User
  ↓
Clicks Edit
  ↓
/edit/<id>/
  ↓
edit_note()
  ↓
Get note using id + request.user
  ↓
Show existing title + content
  ↓
User changes data
  ↓
Submit POST request
  ↓
Update note.title
Update note.content
  ↓
note.save()
  ↓
Database updated
  ↓
redirect("home")
  ↓
Updated note displayed
```

---

# 4. DELETE — Delete a Note

| File                                     | Action                                                               |
| ---------------------------------------- | -------------------------------------------------------------------- |
| `notes/views.py`                         | Created `delete_note()` view to retrieve and delete the user's note. |
| `notes/urls.py`                          | Added `/delete/<int:id>/` URL.                                       |
| `notes/templates/notes/delete_note.html` | Created delete confirmation page.                                    |
| `notes/templates/notes/home.html`        | Added `Delete` button/link to each note.                             |

### Delete Flow

```text
User
  ↓
Clicks Delete
  ↓
/delete/<id>/
  ↓
delete_note()
  ↓
Get note using id + request.user
  ↓
Show confirmation page
  ↓
User confirms deletion
  ↓
POST request
  ↓
note.delete()
  ↓
Note removed from database
  ↓
redirect("home")
  ↓
Home displayed without deleted note
```

---

# Overall NotesApp CRUD Flow

```text
                     NOTES APP
                         │
                         ↓
                   User Logs In
                         │
                         ↓
                   request.user
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       CREATE           READ          UPDATE
          │              │              │
          ↓              ↓              ↓
   Form submitted    Home page      Click Edit
          │              │              │
          ↓              ↓              ↓
   request.POST     filter(user)    Get note
          │              │              │
          ↓              ↓              ↓
Note.objects.create   Display       Modify fields
          │              │              │
          ↓              │              ↓
      Database           │         note.save()
                         │              │
                         │              ↓
                         │          Database
                         │
                         └──────────────┐
                                        │
                                        ↓
                                      DELETE
                                        │
                                        ↓
                                   Click Delete
                                        │
                                        ↓
                                   Get note
                                        │
                                        ↓
                                  Confirmation
                                        │
                                        ↓
                                  note.delete()
                                        │
                                        ↓
                                     Database
```

---

# CRUD Methods Used

```text
CREATE → Note.objects.create()
READ   → Note.objects.filter()
UPDATE → note.save()
DELETE → note.delete()
```

## User-specific protection

```text
CREATE
→ user=request.user

READ
→ filter(user=request.user)

UPDATE
→ get_object_or_404(Note, id=id, user=request.user)

DELETE
→ get_object_or_404(Note, id=id, user=request.user)
```

This ensures each logged-in user can work only with **their own notes**.

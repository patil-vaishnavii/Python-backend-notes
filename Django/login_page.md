# Login page roadmap
```
1. User visits Register page
        ↓
2. User fills the registration form
        ↓
3. User account is created
        ↓
4. User visits Login page
        ↓
5. Django authenticates the credentials
        ↓
6. Django creates a session
        ↓
7. User can access protected pages
        ↓
8. User logs out
        ↓
9. Session is destroyed
```
## For Login page
```
User clicks Login
        │
        ▼
login URL
        │
        ▼
authenticate()
        │
        ▼
login()
        │
        ▼
Session Created
        │
        ▼
request.user
```

## For Sign up page
```
User clicks Sign Up
        │
        ▼
register URL
        │
        ▼
register_view()
        │
        ▼
UserCreationForm
        │
        ▼
Validate data
        │
        ▼
Create User object
        │
        ▼
Save into database
```
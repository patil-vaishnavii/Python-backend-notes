# Complete Request Flow
```
Browser
   │
   ▼
HTTP Request
   │
   ▼
Project urls.py
   │
   ▼
App urls.py
   │
   ▼
View
   │
   ▼
Model (optional)
   │
   ▼
Database
   │
   ▼
View
   │
   ▼
Template
   │
   ▼
Browser (Response)
```
# Complete Authentication Flow
```
                User opens browser
                       │
                       ▼
               htp://127.0.0.1/login/
                       │
                       ▼
              Project urls.py
                       │
             include(accounts.urls)
                       │
                       ▼
              accounts/urls.py
                       │
           path("login/", login_view)
                       │
                       ▼
             accounts/views.py
                       │
             login_view(request)
                       │
              ┌────────┴─────────┐
              │                  │
             GET                POST
              │                  │
              ▼                  ▼
      Render login.html     authenticate()
                                   │
                                   ▼
                             Check auth_user
                                   │
                           Credentials valid?
                              │           │
                             Yes          No
                              │           │
                              ▼           ▼
                      login(request,user) Error Message
                              │
                              ▼
                       Session Created
                              │
                              ▼
                         Dashboard

```

***The project urls.py acts like a central dispatcher, while each app's urls.py is responsible only for its own feature.***

 ```
 FoodVerse/
│
├── FoodVerse/
│      └── urls.py      ← Main router
│
├── restaurants/
│      └── urls.py      ← Restaurant routes
│
├── accounts/
│      └── urls.py      ← Authentication routes
│
├── cart/
│      └── urls.py      ← Cart routes
│
└── orders/
       └── urls.py      ← Order routes
```

```
Browser
   │
   ▼
User visits:
htp:/127.0.0.1:8000/register/
   │
   ▼
FoodVerse/urls.py (Project URLs)
   │
   ▼
path("", include("accounts.urls"))
   │
   ▼
accounts/urls.py
   │
   ▼
path("register/", views.register_view, name="register")
   │
   ▼
accounts/views.py
   │
   ▼
def register_view(request):
    return render(request, "accounts/register.html")
   │
   ▼
accounts/templates/accounts/register.html
   │
   ▼
HTML is rendered
   │
   ▼
Response sent back to Browser
```
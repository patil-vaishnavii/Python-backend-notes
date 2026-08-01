```
User registers
   ↓
Django creates User
   ↓
User logs in
   ↓
Django creates session
   ↓
request.user identifies that user
   ↓
User creates Note
   ↓
Note is connected to that user
```
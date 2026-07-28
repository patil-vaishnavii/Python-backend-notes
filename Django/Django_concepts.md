# Models
- Models represent database tables.
- Example:
  ```
    class Restaurant(models.Model):
      name = models.CharField(max_length=100)
      image = models.ImageField(upload_to="restaurants/")
  ```
- Django converts this into a database table.
```
Restaurant Table

id | name | image
-------------------
1  | Pizza Hut | pizza.jpg
2  | KFC       | kfc.jpg
```
# Admin panel
- Admin panel allows managing database objects without writing forms.
```
Admin Panel
      |
      ↓
Add Restaurant
      |
      ↓
Save
```
# Media files
- Files uploaded by users/admin.
- Django automatically stores uploaded images.

Model:
```
image = models.ImageField(upload_to="restaurants/")
```
# Static files
- Files created by developers.
- Examples:
```
CSS
JavaScript
Logo images
```
- Used with:
```
{% load static %}

```
# ImageField
# ForeignKey relationship
- A restaurant has multiple menu items.
- Relationship:
```
Restaurant
      |
      |
      |---- Menu Item
      |
      |---- Menu Item
      |
      |---- Menu Item

```
- One-to-Many relationship.
- Example:
```
class MenuItem(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    price = models.IntegerField()

```
- Database:
- Restaurant:
```
id | name
-----------
1  | Pizza Hut

```
- Menu:
```
id | restaurant_id | name
-------------------------
1  | 1             | Pizza
2  | 1             | Burger
3  | 1             | Pasta

```
- restaurant_id connects both tables.
# URLs Routing
- URL decides which view should run.
- Flow:
```
Browser URL

     |
     ↓

urls.py

     |
     ↓

views.py

     |
     ↓

template.html

```
- Example:
```
path(
'restaurant/<int:id>/',
views.restaurant_detail,
name="restaurant_detail"
)

```
- URL--> restaurant/1/
- passes: id:1 to the view.
# Dynamic URLs
- Instead of creating separate pages we create one template and dynamically change data.
- Example:
```
restaurant/1/
        |
        ↓
Pizza Hut data


restaurant/2/
        |
        ↓
KFC data

```
# Views
- Views contain business logic.
View responsibilities:

- Fetch data
- Process data
- Send data to template

# Templates
# Template inheritance
- Avoid repeating navbar/footer.
- Instead of multiple html pages carrying some similar code.
- Create:
```
base.html
    |
    |
    navbar

```
- Other pages:
{% extends 'base.html' %}
 ***Benefits:***
 - Reusable code.
 - Cleaner templates.
# QuerySets
# Filtering
# GET requests
# Search logic
# Ordering/sorting
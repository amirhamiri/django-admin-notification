# django-admin-notification
django-admin-notification is a Django app to display notification in Django admin panel.
## Installation
- Run `pip install django-admin-notification`
- Add `admin_notification` to `settings.INSTALLED_APPS` **before** `django.contrib.admin`
```python
INSTALLED_APPS = (
    #...
    "admin_notification",
    #...
    "django.contrib.admin",
    #...
)
```
## Settings


`NOTIFICATION_MODELS`: A list of models which you want to get notified about them in the django admin panel. the correct format for each element of the list is `app.model`
```python
NOTIFICATION_MODELS = ['myapp.MyModel']
```

`ADMIN_SITE_BASE_URL`: An string representing the url to django admin page, if you have changed the base url of the admin site in settings.py, the default is `"admin/"`:
```python
ADMIN_SITE_BASE_URL = 'admin_site_base_url/'
```
## Urls
`check_notifications`: This view is needed to keep track of notifications and redirecting to the corresponding models admin page. you must add this view into your urls list.
```python
...
from admin_notification.views import check_notification_view
urlpatterns = [
    path('check/notification', check_notification_view, name="check_notifications"),
    ...
]
```
> Note: You are free to change the url but keep the name the same as it is in the example.

## Run
- Run `python manage.py migrate`
- Restart your application server
- Visit http://127.0.0.1:8000/admin/
- Create an instance of any of the NOTIFICATION_MODELS and enjoy :)
![notif](https://user-images.githubusercontent.com/78421033/182895917-8c9cbc58-03df-48f8-b231-8f8a50c8162f.jpg)
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
- In settings.py:
```python
NOTIFICATION_MODEL = 'myapp.MyModel' # Select the model you want to control, for example: "accounts.Message"
```
- If you have changed the base url of the admin site. in settings.py: 
```python
ADMIN_SITE_BASE_URL = 'admin_site_base_url/' # default is "admin/
```
- In urls.py:
```python
...
from admin_notification.views import check_notification_view
urlpatterns = [
    path('check/notification', check_notification_view, name="check_notifications"),
    ...
]

```
- Run `python manage.py migrate`
- Restart your application server
- Visit http://127.0.0.1:8000/admin/
- Create an instance of the model(NOTIFICATION_MODEL) and enjoy :)
![notif](https://user-images.githubusercontent.com/78421033/182895917-8c9cbc58-03df-48f8-b231-8f8a50c8162f.jpg)
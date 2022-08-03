from django.shortcuts import render, redirect
from admin_notification.models import Notification
from django.conf import settings
from django.contrib import admin

def check_notification_view(request):
    instance = Notification.objects.all().first()
    instance.count = 0
    instance.save()
    model_name = settings.NOTIFICATION_MODEL.split('.')
    try:
        admin_base_url  = settings.ADMIN_SITE_BASE_URL
    except:
        admin_base_url = 'admin/'
    url = f"/{admin_base_url}{model_name[0]}/{model_name[1].lower()}/"
    return redirect(url)
from django.shortcuts import render, redirect
from admin_notification.models import Notification
from django.conf import settings
from django.urls import reverse
from django.contrib import admin

def check_notification_view(request):
    id = request.GET.get("id")
    if id is not None:
        try:
            notification = Notification.objects.get(id=id)
            notification.count = 0
            notification.save()
            return redirect(notification.get_admin_link())
        except Notification.DoesNotExist:
            return reverse("admin:index")
    return reverse("admin:index")
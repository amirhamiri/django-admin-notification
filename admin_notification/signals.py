from django.db.models.signals import post_delete, post_save, pre_save
from django.apps.registry import Apps
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import HttpResponse, redirect
from django.apps import apps as django_apps
from admin_notification.models import Notification
from django.dispatch import receiver

try:
    model = django_apps.get_model(settings.NOTIFICATION_MODEL, require_ready=False)
except ValueError:
    raise ImproperlyConfigured(
        "NOTIFICATION_MODEL must be of the form 'app_label.model_name'"
    )


@receiver(post_save, sender=model)
def post_save_handler(sender, **kwargs):
    if kwargs['created']:
        notification = Notification.objects.all().first()
        notification.count += 1
        notification.save()

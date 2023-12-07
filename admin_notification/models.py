from __future__ import unicode_literals
from django.contrib.auth.models import User
from admin_notification.cache import del_cached_active_item
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_delete, post_save, pre_save
from six import python_2_unicode_compatible
from functools import cached_property


@python_2_unicode_compatible
class Notification(models.Model):
    count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    model = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    def get_admin_link(self):
        app_label = self.model.app_label
        model_name = self.model.model
        url = reverse(f"admin:{app_label}_{model_name}_changelist")
        return url

    def reset_notifications(self):
        self.count = 0
        self.save()

    def __str__(self):
        return "notifications"

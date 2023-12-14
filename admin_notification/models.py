from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_delete, post_save, pre_save
from six import python_2_unicode_compatible
from functools import cached_property
from admin_notification.constants import APP_CACHE, NOTIFICATIONS_CACHE_KEY


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

    def update_to_cache(self) -> dict:
        self.refresh_from_db
        data = APP_CACHE.get(NOTIFICATIONS_CACHE_KEY, None)
        if data is None:
            raise RuntimeError("App cache updated before initialization")
        instance_data = {
            self.model: {
                "id": self.id,
                "count": self.count,
                "model": self.model,
                "url": self.get_admin_link,
            }
        }
        data.update(instance_data)

        data["count"] = sum(
            value["count"] for key, value in data.items() if key != "count"
        )
        print(data, self.count)
        print(f'{data["count"]} += {self.count} - {data[self.model]["count"]}')
        Notification.set_cache_data(data)
        return data

    @staticmethod
    def get_cache_data() -> dict:
        data = APP_CACHE.get(NOTIFICATIONS_CACHE_KEY, None)
        if data is not None:
            return data
        return dict()

    @staticmethod
    def set_cache_data(data: dict) -> dict:
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")
        APP_CACHE.set(NOTIFICATIONS_CACHE_KEY, data, timeout=1000)
        return data

    def __str__(self):
        return "notifications"

# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.cache import cache, caches


def app_cache():
    return caches["admin_notification"] if "admin_notification" in settings.CACHES else cache


def del_cached_active_item():
    app_cache().delete("admin_notification_item")


def get_cached_active_item():
    return app_cache().get("admin_notification_item", None)


def set_cached_active_item(item):
    app_cache().set("admin_notification_item", item)

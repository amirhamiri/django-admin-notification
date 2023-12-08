from django.conf import settings
from django.core.cache import cache, caches


NOTIFICATIONS_CACHE_KEY = "admin_notifications"
APP_CACHE = (
    caches["admin_notification"] if "admin_notification" in settings.CACHES else cache
)

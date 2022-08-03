from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AdminNotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_notification'

    def ready(self):
        from admin_notification.models import Notification
        import admin_notification.signals
        post_migrate.connect(Notification.post_migrate_handler, sender=self)

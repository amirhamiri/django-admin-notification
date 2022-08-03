from __future__ import unicode_literals
from django.contrib.auth.models import User
from admin_notification.cache import del_cached_active_item
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from six import python_2_unicode_compatible


@python_2_unicode_compatible
class Notification(models.Model):
    @staticmethod
    def post_migrate_handler(**kwargs):
        del_cached_active_item()
        Notification.get_active_item()

    @staticmethod
    def post_delete_handler(**kwargs):
        del_cached_active_item()
        Notification.get_active_item()

    @staticmethod
    def post_save_handler(instance, **kwargs):
        del_cached_active_item()
        if instance.active:
            Notification.objects.exclude(pk=instance.pk).update(active=False)
        Notification.get_active_item()

    @staticmethod
    def pre_save_handler(instance, **kwargs):
        if instance.pk is None:
            try:
                obj = Notification.objects.get(count=instance.count)
                if obj:
                    instance.pk = obj.pk
            except Notification.DoesNotExist:
                pass

    @staticmethod
    def get_active_item():
        objs_manager = Notification.objects
        objs_active_qs = objs_manager.filter(active=True)
        objs_active_ls = list(objs_active_qs)
        objs_active_count = len(objs_active_ls)

        if objs_active_count == 0:
            obj = objs_manager.all().first()
            if obj:
                obj.set_active()
            else:
                obj = objs_manager.create()

        elif objs_active_count == 1:
            obj = objs_active_ls[0]

        elif objs_active_count > 1:
            obj = objs_active_ls[-1]
            obj.set_active()

        return obj
    count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)




    def __str__(self):
        return "notifications"




post_delete.connect(Notification.post_delete_handler, sender=Notification)
post_save.connect(Notification.post_save_handler, sender=Notification)
pre_save.connect(Notification.pre_save_handler, sender=Notification)


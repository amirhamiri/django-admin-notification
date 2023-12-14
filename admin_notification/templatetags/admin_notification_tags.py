import django
from django import template
from admin_notification.models import Notification
from admin_notification.serializers import NotificationsSerializer

register = template.Library()

if django.VERSION < (1, 9):
    simple_tag = register.assignment_tag
else:
    simple_tag = register.simple_tag


@simple_tag
def get_admin_notification_item():
    data = NotificationsSerializer().data
    return data


@register.filter
def is_numeric(x):
    return isinstance(x, int)

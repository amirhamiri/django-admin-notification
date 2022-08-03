import django
from django import template
from admin_notification.cache import get_cached_active_item, set_cached_active_item
from admin_notification.models import Notification

register = template.Library()

if django.VERSION < (1, 9):
    simple_tag = register.assignment_tag
else:
    simple_tag = register.simple_tag


@simple_tag(takes_context=True)
def get_admin_notification_item(context):
    item = get_cached_active_item()
    if not item:
        item = Notification.get_active_item()
        set_cached_active_item(item)
    return item




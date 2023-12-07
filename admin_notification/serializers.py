from admin_notification.models import Notification
from django.db.models import Sum


class NotificationsSerializer:
    query_set = Notification.objects.all()
    
    def __init__(self) -> None:
        self.qs_model = self.query_set.model
        self.model_fields = self.qs_model._meta.fields
        
    def data(self):
        count = self.query_set.aggregate(count_sum=Sum("count"))
        result = {
            "result":[
                {"is_update":self.refresh_from_db(x), "id":x.id, "count":x.count, "model":x.model, "url":x.get_admin_link,} for x in self.query_set
            ],
            "count": count['count_sum']
        }
        return result
    
    def refresh_from_db(self, instance):
        try:
            instance.refresh_from_db()
            return True
        except:
            return False

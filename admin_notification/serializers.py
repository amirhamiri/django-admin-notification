from admin_notification.models import Notification
from django.db.models import Sum


class NotificationsSerializer:
    query_set = Notification.objects.all()

    def __init__(self) -> None:
        self.qs_model = self.query_set.model
        self.model_fields = self.qs_model._meta.fields

    def data(self):
        data_ = Notification.get_cache_data()
        if data_ != dict():
            return data_
        print(data_)
        count = self.query_set.aggregate(count_sum=Sum("count"))
        result = {
            x.model: {
                "id": x.id,
                "count": x.count,
                "model": x.model,
                "url": x.get_admin_link,
            }
            for x in self.query_set
        }

        result.update({"count": count["count_sum"]})

        return Notification.set_cache_data(result)

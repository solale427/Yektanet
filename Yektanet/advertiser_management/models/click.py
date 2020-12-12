from django.db import models
from django.db.models import CASCADE, Count
from django.db.models.functions import TruncHour
from django.utils import timezone
from advertiser_management.models import Ad, AdData


class Click(AdData):
    ad = models.ForeignKey(
        verbose_name='شناسه تبلیغ',
        to=Ad,
        related_name='clicks',
        on_delete=CASCADE
    )

    @staticmethod
    def new_click(ad, user_ip):
        Click.objects.create(ad=ad, user_ip=user_ip)

    @staticmethod
    def get_clicks_sum_per_hour():
        return Click.objects.all().annotate(hour=TruncHour('time')).values('ad', 'hour').annotate(
            clicks=Count('id')
        ).order_by('ad')

from django.db import models
from django.db.models import CASCADE, Count
from django.db.models.functions import TruncHour
from django.utils import timezone
from advertiser_management.models import Ad, AdData


class AdView(AdData):
    ad = models.ForeignKey(
        verbose_name='شناسه تبلیغ',
        to=Ad,
        related_name='views',
        on_delete=CASCADE
    )

    @staticmethod
    def increase_views(user_ip):
        ads = Ad.objects.all()
        for ad in ads:
            AdView.objects.create(ad=ad, user_ip=user_ip)

    @staticmethod
    def get_views_sum_per_hour():
        return AdView.objects.all().annotate(hour=TruncHour('created_at')).values('ad', 'hour').annotate(
            views=Count('id')
        ).order_by('ad')

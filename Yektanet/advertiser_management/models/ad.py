from django.db import models
from django.db.models import CASCADE

from advertiser_management.models import BaseAdvertising, Advertiser


class Ad(BaseAdvertising):

    link = models.CharField(
        max_length=200,
        verbose_name='لینک'
    )

    imgUrl = models.CharField(
        max_length=200,
        verbose_name='آدرس تصویر'
    )

    title = models.CharField(
        max_length=50,
        verbose_name='عنوان تبلیغ'
    )

    advertiser = models.ForeignKey(
        verbose_name='تبلیغ کننده',
        to=Advertiser,
        on_delete=CASCADE,
        related_name='ads'
    )

    def __str__(self):
        return self.title

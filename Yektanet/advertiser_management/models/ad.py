from django.db import models
from django.db.models import CASCADE

from advertiser.models import Advertiser


class Ad(models.Model):
    link = models.CharField(
        max_length=200,
        verbose_name='لینک'
    )

    image = models.CharField(
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
        related_name='ads',
        null=True
    )

    approved = models.BooleanField(
        default=False,
        verbose_name='تایید شده'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'

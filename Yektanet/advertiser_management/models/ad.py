from django.db import models

from advertiser_management.models import BaseAdvertising


class Ad(models.Model, BaseAdvertising):

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

    advertiser= models.ForeignKey(

    )
from django.db import models

from advertiser_management.models import BaseAdvertising


class Advertiser(BaseAdvertising):

    name = models.CharField(
        max_length=50,
        verbose_name='عنوان تبلیغ کننده'
    )

    def __str__(self):
        return self.name

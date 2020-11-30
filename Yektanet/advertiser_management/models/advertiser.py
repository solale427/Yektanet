from django.db import models


class Advertiser(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name='عنوان تبلیغ کننده'
    )
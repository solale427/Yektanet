from django.db import models
from django.db.models import CASCADE

from advertiser_management.models import Ad, AdData


class View(AdData):
    ad = models.ForeignKey(
        verbose_name='شناسه تبلیغ',
        to=Ad,
        related_name='views',
        on_delete=CASCADE
    )
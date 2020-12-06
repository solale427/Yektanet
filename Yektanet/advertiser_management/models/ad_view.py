from django.db import models
from django.db.models import CASCADE

from advertiser_management.models import Ad, AdData


class AdView(AdData):
    ad = models.ForeignKey(
        verbose_name='شناسه تبلیغ',
        to=Ad,
        related_name='views',
        on_delete=CASCADE
    )
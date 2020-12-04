from django.db import models
from django.db.models import CASCADE

from advertiser_management.models import Ad, AdData


class Click(AdData):
    ad = models.ForeignKey(
        verbose_name='شناسه تبلیغ',
        to=Ad,
        related_name='clicks',
        on_delete=CASCADE
    )

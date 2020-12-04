from django.db import models


class AdData(models.Model):
    time = models.DateTimeField(
        verbose_name='زمان'
    )
    user_ip = models.GenericIPAddressField(
        verbose_name='آی پی کاربر'
    )

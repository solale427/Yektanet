from django.db import models


class AdData(models.Model):
    created_at = models.DateTimeField(
        verbose_name='زمان',
        auto_now_add=True
    )
    user_ip = models.GenericIPAddressField(
        verbose_name='آی پی کاربر'
    )


from django.db import models


class BaseAdvertising(models.Model):

    clicks = models.IntegerField(
        verbose_name='کلیک ها'
    )

    views = models.IntegerField(
        verbose_name='مشاهده ها'
    )

    class Meta:
        abstract = True
        verbose_name = 'تبلیغات پایه'

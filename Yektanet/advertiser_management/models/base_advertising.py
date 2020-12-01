from django.db import models


class BaseAdvertising(models.Model):

    clicks = models.IntegerField(
        verbose_name='کلیک ها',
        default=0
    )

    views = models.IntegerField(
        verbose_name='مشاهده ها',
        default=0
    )

    def increase_clicks(self):
        self.clicks += 1
        self.save()

    class Meta:
        abstract = True
        verbose_name = 'تبلیغ پایه'
        verbose_name_plural = 'تبلیغات پایه'

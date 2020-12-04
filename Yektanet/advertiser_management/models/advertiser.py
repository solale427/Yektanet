from django.db import models


class Advertiser(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='عنوان تبلیغ کننده'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تبلیغ کننده'
        verbose_name_plural = 'تبلیغ کنندگان'

# Generated by Django 3.0.8 on 2020-12-12 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0013_ad_nadvertiser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='advertiser',
        ),
    ]

# Generated by Django 3.0.8 on 2020-12-12 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser', '0001_initial'),
        ('advertiser_management', '0012_auto_20201212_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='nadvertiser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='advertiser.Advertiser', verbose_name='تبلیغ کننده'),
        ),
    ]

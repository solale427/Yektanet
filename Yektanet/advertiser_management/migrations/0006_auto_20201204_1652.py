# Generated by Django 3.0.8 on 2020-12-04 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0005_ad_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='زمان')),
                ('user_ip', models.GenericIPAddressField(verbose_name='آی پی کاربر')),
            ],
        ),
        migrations.RemoveField(
            model_name='ad',
            name='clicks',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='views',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='clicks',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='views',
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('addata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='advertiser_management.AdData')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='advertiser_management.Ad', verbose_name='شناسه تبلیغ')),
            ],
            bases=('advertiser_management.addata',),
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('addata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='advertiser_management.AdData')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clicks', to='advertiser_management.Ad', verbose_name='شناسه تبلیغ')),
            ],
            bases=('advertiser_management.addata',),
        ),
    ]

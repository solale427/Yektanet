# Generated by Django 3.0.8 on 2020-11-30 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clicks', models.IntegerField(verbose_name='کلیک ها')),
                ('views', models.IntegerField(verbose_name='مشاهده ها')),
                ('name', models.CharField(max_length=50, verbose_name='عنوان تبلیغ کننده')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clicks', models.IntegerField(verbose_name='کلیک ها')),
                ('views', models.IntegerField(verbose_name='مشاهده ها')),
                ('link', models.CharField(max_length=200, verbose_name='لینک')),
                ('imgUrl', models.CharField(max_length=200, verbose_name='آدرس تصویر')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان تبلیغ')),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='advertiser_management.Advertiser', verbose_name='تبلیغ کننده')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

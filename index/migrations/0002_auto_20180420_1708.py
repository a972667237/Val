# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-04-20 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ImageField(default='/static/img/005.jpg', upload_to=b'', verbose_name='cover_image'),
        ),
        migrations.AddField(
            model_name='article',
            name='isShow',
            field=models.BooleanField(default=False, verbose_name='show_cover'),
        ),
    ]

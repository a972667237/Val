# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-04-28 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180423_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='descript',
            field=models.CharField(default=' ', max_length=10000, verbose_name='descirpt'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_auto_20150917_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='trial',
            field=models.BooleanField(default=False),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-28 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isSeller',
            field=models.BooleanField(default=False),
        ),
    ]
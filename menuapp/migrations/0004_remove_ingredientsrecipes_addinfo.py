# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 00:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0003_auto_20171208_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientsrecipes',
            name='addinfo',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-05 05:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('power', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadFile',
        ),
    ]

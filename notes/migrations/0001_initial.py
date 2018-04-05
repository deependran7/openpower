# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-05 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('filename', models.CharField(max_length=100)),
                ('filelink', models.CharField(max_length=1000)),
            ],
        ),
    ]

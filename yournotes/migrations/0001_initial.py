# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-31 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import yournotes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotesUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('institution', models.CharField(max_length=120)),
                ('filename', models.CharField(max_length=120)),
                ('notefile', models.FileField(null=True, upload_to=yournotes.models.upload_location)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

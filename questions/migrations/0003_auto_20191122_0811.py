# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-22 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20191122_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='image',
            field=models.FileField(default=True, upload_to='answers/'),
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.FileField(default=True, upload_to='questions/'),
        ),
    ]

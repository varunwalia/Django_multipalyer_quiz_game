# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-22 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20191122_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.FileField(blank=True, upload_to='answers'),
        ),
    ]
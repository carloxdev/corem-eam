# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-05 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0002_auto_20161128_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]

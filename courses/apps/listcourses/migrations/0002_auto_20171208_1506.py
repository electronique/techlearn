# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-08 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listcourses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='coursenumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
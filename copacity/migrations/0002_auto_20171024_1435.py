# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-24 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copacity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='testing_scope',
            field=models.IntegerField(default=0),
        ),
    ]
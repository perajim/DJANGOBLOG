# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrado',
            name='codigo_postal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
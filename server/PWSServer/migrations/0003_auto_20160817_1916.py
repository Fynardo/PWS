# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PWSServer', '0002_auto_20160816_1717'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Planta',
            new_name='Celda',
        ),
    ]

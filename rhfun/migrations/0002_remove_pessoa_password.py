# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-11 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhfun', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='password',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-01-15 22:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20180115_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionoptions',
            old_name='answer_type',
            new_name='option',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-01-15 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='question_desc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

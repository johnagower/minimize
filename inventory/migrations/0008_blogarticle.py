# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-14 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20171214_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=160)),
                ('content', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-01-21 23:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0015_auto_20180115_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 1, 21, 23, 26, 35, 549485, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='decision',
            field=models.CharField(choices=[('keep', 'Keep'), ('toss', 'Toss'), ('donate', 'Donate'), ('sell', 'Sell'), ('digitize', 'Digitize'), ('other', 'Something else')], default='None', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='joy',
            field=models.CharField(choices=[('none', 'None'), ('some', 'Some'), ('a lot', 'A lot')], default='None', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='last_used',
            field=models.CharField(choices=[('7', 'Past week'), ('31', 'Past month'), ('365', 'Past year'), ('99999', 'More than a year ago')], default='None', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='replacement_cost',
            field=models.CharField(choices=[('10', 'Less than $10'), ('50', 'Less than $50'), ('100', 'Less than $100'), ('99999', 'More than $100'), ('priceless', 'Priceless')], default='None', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 1, 21, 23, 28, 44, 70749, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

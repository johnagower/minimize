# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-01-15 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_questions_question_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={},
        ),
        migrations.AddField(
            model_name='questionoptions',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='inventory.Questions'),
        ),
    ]

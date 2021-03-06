# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-04 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('abilityhemu_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(null=True),
        ),
    ]

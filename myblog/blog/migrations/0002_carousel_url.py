# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-13 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='url',
            field=models.CharField(max_length=200, null=True, verbose_name='\u56fe\u7247\u94fe\u63a5'),
        ),
    ]

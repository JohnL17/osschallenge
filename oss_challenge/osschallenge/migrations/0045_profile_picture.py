# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 11:06
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('osschallenge', '0044_auto_20170522_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=b'/profile-pictures'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-25 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import enumfields.fields
import shuup.core.fields
import shuup.xtheme.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedViewConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_identifier', models.CharField(db_index=True, max_length=64, verbose_name='theme identifier')),
                ('view_name', models.CharField(db_index=True, max_length=64, verbose_name='view name')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('status', enumfields.fields.EnumIntegerField(db_index=True, enum=shuup.xtheme.models.SavedViewConfigStatus, verbose_name='status')),
                ('_data', shuup.core.fields.TaggedJSONField(db_column=b'data', default=dict, verbose_name='internal data')),
            ],
        ),
        migrations.CreateModel(
            name='ThemeSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_identifier', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='theme identifier')),
                ('active', models.BooleanField(db_index=True, default=False, verbose_name='active')),
                ('data', shuup.core.fields.TaggedJSONField(db_column=b'data', default=dict, verbose_name='data')),
            ],
        ),
    ]

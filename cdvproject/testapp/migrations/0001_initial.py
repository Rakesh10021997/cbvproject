# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-07-18 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=5)),
                ('CEO', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=100)),
            ],
        ),
    ]
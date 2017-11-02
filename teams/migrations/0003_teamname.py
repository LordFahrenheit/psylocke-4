# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20171102_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teamname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname_text', models.CharField(max_length=200)),
                ('category', models.ForeignKey(default='hello', on_delete=django.db.models.deletion.CASCADE, to='teams.Category')),
            ],
        ),
    ]
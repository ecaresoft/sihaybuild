# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repo',
            name='slack_channel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='repo',
            name='slack_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('running', 'running'), ('stopped', 'stopped'), ('passed', 'passed'), ('failed', 'failed')], max_length=7),
        ),
    ]
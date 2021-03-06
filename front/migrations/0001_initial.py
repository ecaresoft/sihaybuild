# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=50)),
                ('committer', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('running', 'running'), ('stopped', 'stopped'), ('passed', 'passed'), ('errored', 'errored')], max_length=7)),
                ('log', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('branch_pattern', models.CharField(max_length=50)),
                ('commands', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pipeline',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.Repo'),
        ),
        migrations.AddField(
            model_name='build',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.Repo'),
        ),
    ]

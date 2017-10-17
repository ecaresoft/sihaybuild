# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Repo(models.Model):
    name = models.CharField(max_length=50)

class Build(models.Model):
    BUILD_STATUSES = (
        ('pending', 'pending'),
        ('running', 'running'),
        ('stopped', 'stopped'),
        ('passed', 'passed'),
        ('errored', 'errored'),
    )

    repo = models.ForeignKey(Repo, on_delete=models.CASCADE)
    branch = models.CharField(max_length=50)
    committer = models.CharField(max_length=50)
    status = models.CharField(max_length=7, choices=BUILD_STATUSES)
    log = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Pipeline(models.Model):
    repo = models.ForeignKey(Repo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    branch_pattern = models.CharField(max_length=50)
    commands = models.TextField()

    def get_commands(self):
        return self.commands.split('\n')

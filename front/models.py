# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Repo(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Build(models.Model):
    BUILD_STATUSES = (
        ('pending', 'pending'),
        ('running', 'running'),
        ('stopped', 'stopped'),
        ('passed', 'passed'),
        ('failed', 'failed'),
    )

    repo = models.ForeignKey(Repo, on_delete=models.CASCADE)
    branch = models.CharField(max_length=50)
    committer = models.CharField(max_length=50)
    status = models.CharField(max_length=7, choices=BUILD_STATUSES)
    log = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s/%s: %s" % (self.repo.name, self.branch, self.status)

@python_2_unicode_compatible
class Pipeline(models.Model):
    repo = models.ForeignKey(Repo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    branch_pattern = models.CharField(max_length=50)
    commands = models.TextField()

    def get_commands(self):
        return self.commands.split('\n')

    def __str__(self):
        return "%s (%s)" % (self.name, self.repo)

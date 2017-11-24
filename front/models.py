# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .utils import yaml_load

@python_2_unicode_compatible
class Repo(models.Model):
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=100)
    additional_setup = models.TextField(null=True, blank=True)
    slack_channel = models.CharField(max_length=20, null=True, blank=True)
    slack_token = models.CharField(max_length=100, null=True, blank=True)

    def get_commands(self):
        if self.additional_setup:
            return self.additional_setup.split('\n')
        else:
            None

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
        return "[%s] %s/%s : %s" % (self.committer, self.repo.name, self.branch, self.status)

@python_2_unicode_compatible
class Pipeline(models.Model):
    repo = models.ForeignKey(Repo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    branch_pattern = models.CharField(max_length=50)
    commands = models.TextField()

    def get_commands(self):
        return yaml_load(self.commands)

    def __str__(self):
        return "%s (%s)" % (self.name, self.repo)

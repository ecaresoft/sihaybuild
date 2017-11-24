# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.list import ListView
from .models import Build, Repo
import pdb

class BuildsView(ListView):
    template_name = 'front/builds.html'
    context_object_name = 'builds'

    def get_queryset(self):
        return Build.objects.all()

class BuildView(generic.DetailView):
    model = Build
    template_name = 'front/build.html'

class ReposView(ListView):
    template_name = 'front/repos.html'
    context_object_name = 'repos'

    def get_queryset(self):
        return Repo.objects.all()

class RepoBuildsView(generic.DetailView):
    model = Repo
    template_name = 'front/repo_builds.html'

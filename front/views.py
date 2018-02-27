# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.list import ListView
from .models import Build, Repo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def index(request):
    return redirect('/repos/')

class BuildsView(LoginRequiredMixin, ListView):
    template_name = 'front/builds.html'
    context_object_name = 'builds'

    def get_queryset(self):
        return Build.objects.all()

class BuildView(LoginRequiredMixin, generic.DetailView):
    model = Build
    template_name = 'front/build.html'

class ReposView(LoginRequiredMixin, ListView):
    template_name = 'front/repos.html'
    context_object_name = 'repos'

    def get_queryset(self):
        return Repo.objects.all()

class RepoBuildsView(LoginRequiredMixin, generic.DetailView):
    # TODO: use select_related bc: N+1
    model = Repo
    template_name = 'front/repo_builds.html'

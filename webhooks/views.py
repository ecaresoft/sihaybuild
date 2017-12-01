# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from webhooks import repos
from front.models import Repo, Build
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from json import loads

@csrf_exempt
def index(request):
    payload = loads(request.body)

    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')

    if event == 'push' and payload['deleted']:
        event = 'deleted'

    repo_name, branch, committer = __parse_payload(event, payload)
    repo = __get_repo(repo_name)

    if repo:
        if event == 'push':
            build = Build(repo=repo, branch=branch, committer=committer, status='pending')
            build.save()
            repos.build(build.id)
        elif event == 'pull_request':
            # TODO associate with build
            pass

    return JsonResponse({'status': 'ok'})

def rerun(request, build_id):
    build = get_object_or_404(Build, pk=build_id)
    build.status = 'running'
    build.save()
    repos.build(build.id)
    return render(request, 'webhooks/rerun.html', {'build': build})

def __parse_payload(event, payload):
    repo = payload['repository']['name'] if 'repository' in payload else None
    branch = None
    committer = None

    try:
        if 'ref_type' in payload:
            if payload['ref_type'] == 'branch':
                branch = payload['ref']
        elif 'pull_request' in payload:
            branch = payload['pull_request']['base']['ref']
        elif event in ['push']:
            branch = payload['ref'].split('/', 2)[2]
            committer = payload['pusher']['name']
    except KeyError:
        pass

    return [repo, branch, committer]

def __get_repo(name):
    try:
        return Repo.objects.get(name=name)
    except ObjectDoesNotExist:
        return None

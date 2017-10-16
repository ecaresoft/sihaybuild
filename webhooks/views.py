# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from webhooks import repos

def index(request):
    payload = request.get_json()

    event = request.headers.get('X-GitHub-Event', 'ping')

    if event == 'push' and payload['deleted']:
        event = 'deleted'

    repo, branch = parse_payload(payload)

    if event == 'push':
        repos.build(repo, branch)
    elif event == 'pull_request':
        # TODO associate with build
        pass

    return JsonResponse({'status': 'ok'})

def parse_payload(payload):
    repo = payload['repository']['name'] if 'repository' in payload else None
    branch = None

    try:
        if 'ref_type' in payload:
            if payload['ref_type'] == 'branch':
                branch = payload['ref']
        elif 'pull_request' in payload:
            branch = payload['pull_request']['base']['ref']
        elif event in ['push']:
            branch = payload['ref'].split('/', 2)[2]
    except KeyError:
        pass

    return [repo, branch]

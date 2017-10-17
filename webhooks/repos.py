from subprocess import call
from os import chdir
from simpleci.settings import BASE_DIR
from front.models import Pipeline

def install(source):
    call(['mkdir', '-p', '.repos'])
    chdir('.repos')
    call(['git', 'clone', source])
    chdir(BASE_DIR)

def build(repo, branch):
    if not __is_installed(repo):
        return "Please clone repo before building"

    try:
        __setup(repo, branch)
        __run(repo, branch)
    finally:
        __cleanup()

def __is_installed(repo):
    return call(['test', '-d', ".repos/%s" % repo]) == 0

def __setup(repo, branch):
    chdir(".repos/%s" % repo)
    call(['git', 'fetch', '--prune'])
    call(['git', 'checkout', branch])
    call(['git', 'reset', '--hard', "origin/%s" % branch])

def __run(repo, branch):
    pipeline = __get_pipeline(repo, branch)
    status = 0

    for command in pipeline:
        status = call(command.split(' '))

def __cleanup():
    call(['git', 'checkout', '--', '.'])
    chdir(BASE_DIR)

def __get_pipeline(repo, branch):
    pipelines = Pipeline.objects.filter(
        repo__name=repo,
        branch_pattern__contains=branch
    )

    pipeline = pipelines[0] if len(pipelines) > 0 else Pipeline.objects.get(repo__name=repo, name='default')

    return pipeline.get_commands()

from subprocess import call
from os import chdir
from simpleci.settings import BASE_DIR

def install(source):
    call(['mkdir', '-p', '.repos'])
    chdir('.repos')
    call(['git', 'clone', source])
    chdir(BASE_DIR)

def build(repo, branch):
    if not __is_installed(repo):
        return "Please clone repo before building"

    __setup(repo, branch)
    __run()
    __cleanup()

def __is_installed(repo):
    return call(['test', '-d', ".repos/%s" % repo]) == 0

def __setup(repo, branch):
    chdir(".repos/%s" % repo)
    call(['git', 'fetch', '--prune'])
    call(['git', 'checkout', branch])
    call(['git', 'reset', '--hard', "origin/%s" % branch])

def __run():
    call(['echo', 'meep'])

def __cleanup():
    call(['git', 'checkout', '--', '.'])
    chdir(BASE_DIR)

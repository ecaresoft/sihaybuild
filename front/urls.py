from django.conf.urls import url

from . import views

app_name = 'front'
urlpatterns = [
    # /builds
    url(r'^builds/$', views.BuildsView.as_view(), name='builds'),
    # /repos
    url(r'^repos/$', views.ReposView.as_view(), name='repos'),
    # builds/:id
    url(r'^builds/(?P<pk>[0-9]+)/$', views.BuildView.as_view(), name='build'),
    # /repository/:id/builds
    url(r'^repos/(?P<pk>[0-9]+)/builds/$', views.RepoBuildsView.as_view(), name='repo_builds'),
]

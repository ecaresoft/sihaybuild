from django.conf.urls import url
from . import views

app_name = 'webhooks'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^builds/(?P<build_id>[0-9]+)/rerun/$', views.rerun, name='rerun')
]

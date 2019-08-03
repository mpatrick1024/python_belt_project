from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.job_new),
    url(r'^create$', views.job_create),
    url(r'^cancel$', views.job_cancel),
    url(r'^(?P<job_id>\d+)$', views.job_show),
    url(r'^edit/(?P<job_id>\d+)$', views.job_edit),
    url(r'^(?P<job_id>\d+)/update$', views.job_update),
    url(r'^(?P<job_id>\d+)/destroy$', views.job_destroy),
    url(r'^(?P<job_id>\d+)/giveup$', views.job_giveup),
    url(r'^(?P<job_id>\d+)/add$', views.job_add)
]
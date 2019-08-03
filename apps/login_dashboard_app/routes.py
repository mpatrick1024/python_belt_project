from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^register$', views.create_user),
    url(r'^login$', views.get_user),
    url(r'^logout$', views.destroy),
    url(r'^dashboard$', views.dashboard)
]
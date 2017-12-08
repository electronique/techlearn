from django.conf.urls import url
from . import views        
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$', views.add),
    url(r'^detailinfo/(?P<id>\d+)$', views.detailinfo),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^remove/delete/(?P<id>\d+)$', views.delete),
  ]
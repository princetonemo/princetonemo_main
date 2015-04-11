from django.conf.urls import patterns, url
from emo import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
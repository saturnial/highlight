from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'create', views.create, name='create'),
    url(r'feed', views.feed, name='feed'),
    url(r'', views.index, name='index'),
)

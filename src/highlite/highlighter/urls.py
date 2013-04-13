from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'feed', views.feed, name='feed'),
    url(r'', views.index, name='index'),
)



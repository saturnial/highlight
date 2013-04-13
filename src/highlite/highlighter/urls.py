from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'create', views.CreateHighlight.as_view(), name='create'),
    url(r'feed', views.feed, name='feed'),
    url(r'', views.index, name='index'),
)

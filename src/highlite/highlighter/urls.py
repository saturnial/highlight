from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'', views.index, name='index'),
    url(r'feed/', views.feed, name='feed'),
    url(r'create/', views.create, name='create'),
)

from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'create', views.CreateHighlight.as_view(), name='create'),
    url(r'feed', views.HighlightFeed.as_view(), name='feed'),
    url(r'', views.Index.as_view(), name='index'),
)

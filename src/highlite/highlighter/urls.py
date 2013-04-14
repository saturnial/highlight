from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

import views

urlpatterns = patterns('',
    url(r'create', login_required(views.CreateHighlight.as_view()), name='create'),
    url(r'feed', login_required(views.HighlightFeed.as_view()), name='feed'),
    url(r'highlight/(?P<pk>\d+)', login_required(views.HighlightDetailView.as_view()), name='detail'),
    url(r'', views.Index.as_view(), name='index'),
)

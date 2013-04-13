from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='lite/')), 
     url(r'lite/', include('highlite.highlighter.urls')),
    url(r'^facebook/login', 'highlite.facebook.views.login'),
    url(r'^facebook/authentication_callback$', 'highlite.facebook.views.authentication_callback'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),

    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

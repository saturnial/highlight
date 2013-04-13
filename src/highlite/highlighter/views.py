from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

import forms
import foursquare
import logging

def index(request):
  return render_to_response('index.html', {})

def feed(request):
  facebook_profile = request.user.get_profile().get_facebook_profile()
  return render_to_response('feed.html', {'facebook_profile': facebook_profile})

def create(request):
  if request.method == 'POST':
    form = forms.CreateHighlight(request.POST)
    if form.is_valid():
      return HttpResponseRedirect('/')
  else:
    form = forms.CreateHighlight()
    #fsq_auth_token = request.session.get('fsq_access_token')
    #logging.info(fsq_auth_token)
    #fsq_client = foursquare.Foursquare(access_token=fsq_auth_token)

    #coffee_places = fsq_client.venues.search(params={'query': 'coffee',
    #                                                 'near': 'San Francisco, CA'})
  return render_to_response('create.html', {
      'form': form,
      #'coffee_search': coffee_places
  })

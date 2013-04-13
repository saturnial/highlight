from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.template import RequestContext

import forms
import foursquare
import logging

def index(request):
  return render_to_response('index.html', {})

def feed(request):
  facebook_profile = request.user.get_profile().get_facebook_profile()
  return render_to_response('feed.html', {'facebook_profile': facebook_profile})

class CreateHighlight(View):
  """Class-based view for handling the create highlight process."""

  def get(self, request):
    form = forms.CreateHighlight()
    return render_to_response('create.html',
                              {'form': form},
                              context_instance=RequestContext(request))

  def post(self, request):
    form = forms.CreateHighlight(request.POST)
    if form.is_valid():
      new_highlight = form.save()
      return HttpResponseRedirect('/lite/create')
    else:
      return render_to_response('create.html', {'form': form})

    #fsq_auth_token = request.session.get('fsq_access_token')
    #logging.info(fsq_auth_token)
    #fsq_client = foursquare.Foursquare(access_token=fsq_auth_token)

    #coffee_places = fsq_client.venues.search(params={'query': 'coffee',
    #                                                 'near': 'San Francisco, CA'})
      #'coffee_search': coffee_places

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.template import RequestContext
from django.contrib.auth.models import User

from models import Highlight
import forms
import foursquare
import logging

class Index(View):
  """Class-based view for handling the initial login."""

  def get(self, request):
    logged_in = request.user.is_authenticated()
    if logged_in:
      return HttpResponseRedirect('/lite/create')

    return render_to_response('index.html',
                              {})

class HighlightFeed(ListView):
  """Class-based generic view listing out all highlights."""

  context_object_name = 'highlights'
  queryset = Highlight.objects.all()
  template_name = 'feed.html'


class CreateHighlight(View):
  """Class-based view for handling the create highlight process."""

  def get(self, request):
    facebook_profile = request.user.get_profile().get_facebook_profile()
    form = forms.CreateHighlight()
    return render_to_response('create.html',
                              {'form': form,
                               'facebook_profile': facebook_profile},
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

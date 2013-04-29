from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.template import RequestContext

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
    return render_to_response('index.html', {})

class HighlightFeed(ListView):
  """Class-based generic view listing out all highlights."""

  context_object_name = 'highlights'
  template_name = 'feed.html'

  def get_queryset(self):
    return Highlight.objects.filter(user=self.request.user)

  def get_context_data(self, **kwargs):
    context = super(HighlightFeed, self).get_context_data(**kwargs)
    facebook_profile = self.request.user.get_profile()
    context['facebook_profile'] = facebook_profile
    return context

class HighlightDetailView(DetailView):
  """Class-based generic view detailing an individual highlight."""

  context_object_name = 'highlight'
  queryset = Highlight.objects.all()
  template_name = "highlight_detail.html"

def get_possible_venues(request, query):
  fsq_auth_token = request.session.get('fsq_access_token')
  fsq_client = foursquare.Foursquare(access_token=fsq_auth_token)
  query_results = fsq_client.venues.search(params={'query': query,
                                                   'near': 'San Francisco, CA',
                                                   'limit': 5})
  print query_results
  response = []
  for venue in query_results:
    response.append(venue['response']['checkins']['items']['venue']['name'])
  return json.dumps(response)

class CreateHighlight(View):
  """Class-based view for handling the create highlight process."""

  def get(self, request):
    if Highlight.objects.filter(user=request.user).exists():
      most_recent_highlight = Highlight.objects.latest()
    else:
      most_recent_highlight = None
    facebook_profile = request.user.get_profile()
    form = forms.CreateHighlight()
    fsq_auth_token = request.session.get('fsq_access_token')
    if not fsq_auth_token:
      return HttpResponseRedirect('/foursq_auth/auth')
    return render_to_response('create.html',
                              {'form': form,
                               'facebook_profile': facebook_profile,
                               'recent_highlight': most_recent_highlight},
                              context_instance=RequestContext(request))

  def post(self, request):
    form = forms.CreateHighlight(request.POST)
    if form.is_valid():
      new_highlight = form.save(commit=False)
      new_highlight.user = request.user
      new_highlight.save()
      return HttpResponseRedirect('/lite/create')
    else:
      return render_to_response('create.html', {'form': form})
      recent_highlight = Highlight.objects.filter(user=request.user).latest()
      facebook_profile = request.user.get_profile()
      return render_to_response('create.html',
                                {'form': form,
                                 'facebook_profile': facebook_profile,
                                 'recent_highlight': recent_highlight},
                                context_instance=RequestContext(request))

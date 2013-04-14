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
  queryset = Highlight.objects.all()
  template_name = 'feed.html'

  def get_context_data(self, **kwargs):
    context = super(HighlightFeed, self).get_context_data(**kwargs)
    profile = self.request.user.get_profile()
    context['facebook_profile'] = profile
    return context

class HighlightDetailView(DetailView):
  """Class-based generic view detailing an individual highlight."""

  context_object_name = 'highlight'
  queryset = Highlight.objects.all()
  template_name = "highlight_detail.html"

class CreateHighlight(View):
  """Class-based view for handling the create highlight process."""

  def get(self, request):
    profile = request.user.get_profile()
    recent_highlight = Highlight.objects.filter(user=request.user).latest()
    facebook_profile = request.user.get_profile()
    form = forms.CreateHighlight()

    fsq_auth_token = request.session.get('fsq_access_token')
    if not fsq_auth_token:
      return HttpResponseRedirect('/foursq_auth/auth')
    fsq_client = foursquare.Foursquare(access_token=fsq_auth_token)
    query_results = fsq_client.venues.search(params={'query': 'bar',
                                                     'near': 'San Francisco, CA'})
    return render_to_response('create.html',
                              {'form': form,
                               'query_results': query_results},
                               'facebook_profile': facebook_profile,
                               'recent_highlight': recent_highlight},
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

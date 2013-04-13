from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

import forms

def index(request):
  return render_to_response('index.html', {})

def feed(request):
  facebook_profile = request.user.get_profile().get_facebook_profile()
  return render_to_response('feed.html', {})

def create(request):
  if request.method == 'POST':
    form = forms.CreateHighlight(request.POST)
    if form.is_valid():
      return HttpResponseRedirect('/thanks/')
    else:
      form = forms.CreateHighlight()
    return render_to_response(request, 'create.html', {
        'form': form,
    })

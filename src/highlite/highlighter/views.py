from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

def index(request):
  return render_to_response('index.html', {}) 

def feed(request):
  facebook_profile = request.user.get_profile().get_facebook_profile() 
  return render_to_response('feed.html', {})


def create(request):
  return render_to_response('create.html', {})

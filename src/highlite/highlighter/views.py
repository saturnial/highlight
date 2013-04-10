from django.shortcuts import render_to_response

def index(request):
  return render_to_response('index.html', {}) 


def feed(request):
  return render_to_response('feed.html', {})


def create(request):
  return render_to_response('create.html', {})

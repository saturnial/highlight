import urllib
import urllib2
import json

from django.http import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

CLIENT_ID = 'AALFWGJGNEAO5KREE3KQI2YH0I1T3SHY5VZNOJFGK25E55PU'
CLIENT_SECRET = 'XXJJKVEB1QQLJSFFAU53KB1O3JBBFQ503BBMV5L5BA5XXFGN'

request_token_url = 'https://foursquare.com/oauth2/authenticate'
access_token_url = 'https://foursquare.com/oauth2/access_token'
redirect_url = 'http://localhost:8000/foursq_auth/callback'

def callback( request ):
    # get the code returned from foursquare
    code = request.GET.get('code')

    # build the url to request the access_token
    params = { 'client_id' : CLIENT_ID,
               'client_secret' : CLIENT_SECRET,
               'grant_type' : 'authorization_code',
               'redirect_uri' : redirect_url,
               'code' : code}
    data = urllib.urlencode(params)
    req = urllib2.Request(access_token_url, data)

    # request the access_token
    response = urllib2.urlopen(req)
    access_token = json.loads(response.read( ))
    access_token = access_token['access_token']

    # store the access_token for later use
    request.session['fsq_access_token'] = access_token
    return HttpResponseRedirect(reverse('index'))

def unauth( request ):
    # clear any tokens and logout
    request.session.clear( )
    logout( request )
    return HttpResponseRedirect( reverse( 'main' ) )  

def auth( request ):
    # build the url to request
    params = {'client_id' : CLIENT_ID,
            'response_type' : 'code',
            'redirect_uri' : redirect_url }
    data = urllib.urlencode( params )
    # redirect the user to the url to confirm access for the app
    return HttpResponseRedirect( '%s?%s' % ( request_token_url, data  ) )

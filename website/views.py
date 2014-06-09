from django.shortcuts import render_to_response
from website.models import Service

# Create your views here.

def index(request):
    return render_to_response('website/index.html', {'page': 'index', 'header': ''})

def drbetty(request):
    services = Service.objects.filter(display=True)
    return render_to_response('website/drbetty.html', {'page': 'drbetty', 'header': 'Dr. Betty', 'services': services})

def health(request):
    return render_to_response('website/health.html', {'page': 'health', 'header': 'Health'})

def sports(request):
    return render_to_response('website/sports.html', {'page': 'sports', 'header': 'Sports'})

def lifecoach(request):
    return render_to_response('website/lifecoach.html', {'page': 'lifecoach', 'header': 'Life Coach'})

def downloads(request):
    return render_to_response('website/downloads.html', {'page': 'downloads', 'header': 'Downloads'})

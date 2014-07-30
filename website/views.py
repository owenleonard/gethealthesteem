from datetime import date
from django.shortcuts import render_to_response, get_object_or_404
from website.models import Service, Event

# helper methods
def events():
    return Event.objects.filter(display=True).filter(starttime__gte=date.today()).order_by('starttime')[:5]

# Create your views here.
def index(request):
    return render_to_response('website/index.html', {'page': 'index', 'header': '', 'events': events()})

def drbetty(request):
    services = Service.objects.filter(display=True)
    return render_to_response('website/drbetty.html', {'page': 'drbetty', 'header': 'Dr. Betty', 'services': services, 'events': events()})

def health(request):
    return render_to_response('website/health.html', {'page': 'health', 'header': 'Health', 'events': events()})

def sports(request):
    return render_to_response('website/sports.html', {'page': 'sports', 'header': 'Sports', 'events': events()})

def lifecoach(request):
    return render_to_response('website/lifecoach.html', {'page': 'lifecoach', 'header': 'Life Coach', 'events': events()})

def downloads(request):
    return render_to_response('website/downloads.html', {'page': 'downloads', 'header': 'Downloads', 'events': events()})

def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id, display=True)
    return render_to_response('website/event.html', {'page': 'event', 'header': 'Event', 'events': events(), 'event': event})
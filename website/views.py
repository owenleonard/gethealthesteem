from datetime import date
from django.shortcuts import render_to_response, get_object_or_404
from website.models import Service, Event, Content

# helper methods
def events():
    return Event.objects.filter(display=True).filter(starttime__gte=date.today()).order_by('starttime')[:5]

def slogan():
    return Content.objects.filter(title="slogan").first()

# Create your views here.
def index(request):
    content = Content.objects.filter(title="home").first()
    return render_to_response('website/index.html', {'header': '', 'events': events(), 'slogan': slogan(), 'content': content})

def drbetty(request):
    services = Service.objects.filter(display=True)
    content = Content.objects.filter(title="profile").first()
    return render_to_response('website/drbetty.html', {'header': 'Dr. Betty', 'services': services, 'events': events(), 'slogan': slogan(), 'content': content})

def health(request):
    return render_to_response('website/health.html', {'header': 'Health', 'events': events(), 'slogan': slogan()})

def sports(request):
    return render_to_response('website/sports.html', {'header': 'Sports', 'events': events(), 'slogan': slogan()})

def lifecoach(request):
    return render_to_response('website/lifecoach.html', {'header': 'Life Coach', 'events': events(), 'slogan': slogan()})

def downloads(request):
    return render_to_response('website/downloads.html', {'header': 'Downloads', 'events': events(), 'slogan': slogan()})

def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id, display=True)
    return render_to_response('website/event.html', {'header': 'Event', 'events': events(), 'slogan': slogan(), 'event': event})
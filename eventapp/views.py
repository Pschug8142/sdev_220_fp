from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy
# from django.template import loader
from .models import EventPost
from .forms import ToonEntry, EventEntry


def index(request):
    latest_events = EventPost.objects.order_by("-event_date")[:5]
    # output = ", ".join([event.title for event in latest_events])
    # template = loader.get_template("eventapp/events_list.html")
    context = {
        "latest_events": latest_events,
    }
    return render(request, "eventapp/events_list.html", context)


def detail(request, event_id):
    return HttpResponse("You're looking at event %s." % event_id)

def toon_view(request):
    context = {}

    form = ToonEntry(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()     # save it to the Toon model
    
    context['form'] = form
    success_url = reverse_lazy('login')
    return render(request, "eventapp/toons.html", context)

def event_entry(request):
    context = {}

    form = EventEntry(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "eventapp/event.html", context)
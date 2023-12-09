from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import EventPost


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
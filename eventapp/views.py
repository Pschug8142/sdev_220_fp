from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy
# from django.template import loader
from .models import EventPost, Toon
from .forms import ToonEntry, EventEntry


def index(request):
    print(f'views.py index')

    latest_events = EventPost.objects.order_by("-event_date")[:5]
    toons = Toon.objects.all()
    # output = ", ".join([event.title for event in latest_events])
    # template = loader.get_template("eventapp/events_list.html")
    context = {
        "latest_events": latest_events,
        "toons": toons,
    }
    return render(request, "eventapp/events_list.html", context)


def detail(request, pk):
    event = get_object_or_404(EventPost, pk=pk)
    print(f'views.py detail(key:{pk})')
    context = {
        "event": event,
    }
    return render(request, "eventapp/detail.html", context)

def toon_view(request):
    print(f'views.py toon_view')

    context = {}

    form = ToonEntry(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()     # save it to the Toon model
    
    context['form'] = form
    # success_url = reverse_lazy('login')
    return render(request, "eventapp/toons.html", context)

def event_entry(request):
    print(f'views.py event_entry)')

    context = {}

    form = EventEntry(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "eventapp/event.html", context)
    

def add_participant(request, pk):
    print(f'views.py add {pk}')
    event = EventPost.objects.get(pk=pk)
    event.add_signup(user=request.user)
    return redirect('eventapp/detail', pk=pk)

def del_participant(request, pk):
    event = EventPost.objects.get(pk=pk)
    event.del_signup(request.user)
    return redirect('eventapp/detail', pk=pk)

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy  # unsure about how to get this working below for redirect
from .models import EventPost, Toon
from .forms import ToonEntry, EventEntry


def index(request):
    """View for the main page.  Provides a list of 'latest events' """
    # Currently, the page also displays a list of all characters registered on the site for debugging
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
    """View for the Event detail page.  Should provide the event object and a roster"""
    # roster not currently working.  Lots of debugging stuff below
    event = get_object_or_404(EventPost, pk=pk)
    toon = Toon.objects.get(player_name=request.user.id)
    toon.get_raiderio()         # this works
    print(toon.player_name)
    toons = Toon.objects.all()
    print(f'views.py detail(key:{pk})')
    print(f'views.py request.user: {request.user}')
    roster = event.get_participants()   # currently None
    print(roster)
    context = {
        "event": event,
        "toon": toon,
        "toons": toons,
    }
    return render(request, "eventapp/detail.html", context)

def toon_view(request):
    """view for the Toon ModelForm form."""
    print(f'views.py toon_view')

    context = {}

    form = ToonEntry(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()     # save it to the Toon model
    
    context['form'] = form
    # success_url = reverse_lazy('login')
    return render(request, "eventapp/toons.html", context)

def event_entry(request):
    """View for creating a new event form."""
    print(f'views.py event_entry)')

    context = {}

    form = EventEntry(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "eventapp/event.html", context)
    

def add_participant(request, pk):
    """View to add a participant to an event roster."""
    # Not currently working
    print(f'views.py add {pk}')
    toon = Toon.objects.get(player_name=request.user.id)
    event = EventPost.objects.get(pk=pk)
    event.add_signup(user=request.user.id)
    return redirect('eventapp/detail', pk=pk)

def del_participant(request, pk):
    """View to remove a participant from an event roster."""
    # Not currently working
    event = EventPost.objects.get(pk=pk)
    event.del_signup(request.user)
    return redirect('eventapp/detail', pk=pk)












# from django.shortcuts import render
# from django.shortcuts import render, get_object_or_404, redirect

# # Create your views here.
# from django.http import HttpResponse
# from django.urls import reverse_lazy
# # from django.template import loader
# from .models import EventPost, Toon
# from .forms import ToonEntry, EventEntry


# def index(request):
#     print(f'views.py index')

#     latest_events = EventPost.objects.order_by("-event_date")[:5]
#     toons = Toon.objects.all()
#     # output = ", ".join([event.title for event in latest_events])
#     # template = loader.get_template("eventapp/events_list.html")
#     context = {
#         "latest_events": latest_events,
#         "toons": toons,
#     }
#     return render(request, "eventapp/events_list.html", context)


# def detail(request, pk):
#     event = get_object_or_404(EventPost, pk=pk)
#     print(f'views.py detail(key:{pk})')
#     context = {
#         "event": event,
#     }
#     return render(request, "eventapp/detail.html", context)

# def toon_view(request):
#     print(f'views.py toon_view')

#     context = {}

#     form = ToonEntry(request.POST or None, request.FILES or None)

#     if form.is_valid():
#         form.save()     # save it to the Toon model
    
#     context['form'] = form
#     # success_url = reverse_lazy('login')
#     return render(request, "eventapp/toons.html", context)

# def event_entry(request):
#     print(f'views.py event_entry)')

#     context = {}

#     form = EventEntry(request.POST or None, request.FILES or None)
    
#     if form.is_valid():
#         form.save()

#     context['form'] = form
#     return render(request, "eventapp/event.html", context)
    

# def add_participant(request, pk):
#     print(f'views.py add {pk}')
#     event = EventPost.objects.get(pk=pk)
#     event.add_signup(user=request.user)
#     return redirect('eventapp/detail', pk=pk)

# def del_participant(request, pk):
#     event = EventPost.objects.get(pk=pk)
#     event.del_signup(request.user)
#     return redirect('eventapp/detail', pk=pk)
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:event_id>/", views.detail, name="detail"),
    path("toons", views.toon_view, name="toons"),
    path("event", views.event_entry, name="event"),
]
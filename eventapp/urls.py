from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("toons", views.toon_view, name="toons"),
    path("event", views.event_entry, name="event"),
    path("<int:pk>/", views.add_participant, name="add_participant"),
    path("<int:pk>/", views.del_participant, name="del_participant"),
]
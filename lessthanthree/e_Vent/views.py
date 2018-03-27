from django.shortcuts import render

# Create your views here.
from .models import Location, Tag, Price, Popularity, Event, User
from django.views import generic

class IndexView(generic.ListView):
    model = Event
    template_name = 'index.html'

class EventDetailView(generic.DetailView):
    model = Event
    template_name = "e_Vent/eventDetails.html"


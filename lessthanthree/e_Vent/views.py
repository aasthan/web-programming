from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Location, Tag, Price, Popularity, Event, User

class IndexView(generic.ListView):
    model = Event
    template_name = 'index.html'

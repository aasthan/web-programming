from django.shortcuts import render

# Create your views here.
from .models import Location, Tag, Price, Popularity, Event, User
from django.views import generic

class IndexView(generic.ListView):
    model = Event
    template_name = 'index.html'

from django.core import serializers

class EventDetailView(generic.DetailView):
	model = Event
	template_name = "e_Vent/eventDetails.html"

	# Combining Detail view and retrieve list of event objects
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['event_list'] = Event.objects.all()
		return context

	def get_loc(request):
		query_set = Event.objects.values('location')
		list(query_set)
		str =  str(query_set)


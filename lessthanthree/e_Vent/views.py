from django.shortcuts import render

# Create your views here.
from .models import Location, Tag, Price, Popularity, Event, Profile
from django.views import generic
import operator
from django.db.models import Q
from functools import reduce

def indexView(request):
	"""
	View function for the home page
	"""
	#Generate counts of some of the main objects
	num_events = Event.objects.all().count()
	events = Event.objects.all()
	num_profiles = Profile.objects.all().count()
	num_location = Location.objects.all().count()
	popular_events = Event.objects.filter(saves__gte = 2)

	return render(
		request,
		'index.html',
		context={'events':events,'num_events':num_events,'num_profiles':num_profiles,'num_location':num_location,'popular_events':popular_events},

		)

def browseEventsView(request):

	allEvents = Event.objects.all()

	paginate_by = 18

	return render(
		request,
		'e_Vent/browseEvent.html',
		context={'allEvents':allEvents},

		)

def filterEventByPriceView(request):
	allEvents = Event.objects.all()
	freePrice = Event.objects.filter(price = 0)
	lessThanTwenty = Event.objects.filter(price__lt = 20)
	twentyToFifty = Event.objects.filter(price__gte = 20, price__lte = 50)
	greaterThanFifty = Event.objects.filter(price__gte = 50)

	return render(
		request,
		'e_Vent/filterEventByPrice.html',
		context={'freePrice':freePrice, 'lessThanTwenty': lessThanTwenty, 'twentyToFifty': twentyToFifty, 'greaterThanFifty': greaterThanFifty},
		)

def filterEventByLocationView(request):
	locationAmherst = Event.objects.filter(location__name__icontains = "amherst")
	locationUMass = Event.objects.filter(location__name__icontains = "umass")
	locationMtHolyoke = Event.objects.filter(location__name__icontains = "holyoke")
	locationHampshire = Event.objects.filter(location__name__icontains = "hampshire")
	locationSmith = Event.objects.filter(location__name__icontains = "smith")

	return render(
		request,
		'e_Vent/filterEventByLocation.html',
		context={'locationAmherst':locationAmherst, 'locationUMass': locationUMass, 'locationMtHolyoke': locationMtHolyoke, 'locationHampshire': locationHampshire, 'locationSmith': locationSmith},
		)

def filterEventByCategoryView(request):
	tagCultural = Event.objects.filter(tag__name__icontains = "cultural")
	tagSport = Event.objects.filter(tag__name__icontains = "sport")

	return render(
		request,
		'e_Vent/filterEventByCategory.html',
		context={'tagCultural':tagCultural, 'tagSport': tagSport},
		)


from django.core import serializers

class EventDetailView(generic.DetailView):
	model = Event
	template_name = "e_Vent/eventDetails.html"

	# Combining Detail view and retrieve list of event objects
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(EventDetailView, self).get_context_data(**kwargs)
		#get tag from current event
		currentTag = super(EventDetailView, self).get_object().display_tag()
		print (currentTag)
		#create a list with events that have same tags
		context['event_list'] = Event.objects.filter(tag__name__icontains = currentTag)
		return context

	def get_loc(request):
		query_set = Event.objects.values('location')
		list(query_set)
		str =  str(query_set)

from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

class PostSaveToggle(LoginRequiredMixin, generic.RedirectView):
	def get_redirect_url(self, pk):
		obj = get_object_or_404(Event, pk=pk)
		print(pk)
		url_ = obj.get_absolute_url()
		user = self.request.user
		if user in obj.saves.all():
			obj.saves.remove(user)
		else:
			obj.saves.add(user)
		return url_

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class PostSaveAPIToggle(LoginRequiredMixin, APIView):
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)
	def get(self, request, pk, format=None):
		obj = get_object_or_404(Event, pk=pk)
		url_ = obj.get_absolute_url()
		user = self.request.user
		updated = False
		saved = False
		if user in obj.saves.all():
			saved = False
			obj.saves.remove(user)
		else:
			saved = True
			obj.saves.add(user)
		updated = True
		data = {"updated": updated, "saved": saved}
		return Response(data)

class EventSearchView(generic.ListView):
    model = Event
    template_name = 'e_Vent/search.html'
    def get_queryset(self):
        result = super(EventSearchView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(reduce(operator.and_,(Q(title__icontains=q) for q in query_list)))
        return result

from django.views.generic import ListView
class YourEventsView(LoginRequiredMixin, generic.ListView):
	model = Event
	template_name ='e_Vent/profile.html'
	context_object_name = 'event_made'
	login_url = '/accounts/login/'
	redirect_field_name = 'redirect_to'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the events
		context['event_made'] = Event.objects.filter(profile=self.request.user)
		return context
class SavedEventsView(LoginRequiredMixin, generic.ListView):
	model = Event
	template_name ='e_Vent/profile.html'
	context_object_name = 'event_made'
	login_url = '/accounts/login/'
	redirect_field_name = 'redirect_to'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['event_saved'] = Event.objects.filter(saves=self.request.user)
		return context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
class EventFormView(LoginRequiredMixin, generic.ListView):
	model = Event
	template_name = 'e_Vent/form.html'
	login_url = '/accounts/login/'
	redirect_field_name = 'redirect_to'

class LoginView(generic.ListView):
	model = Event
	template_name = 'e_Vent/logIn.html'

class SignupView(generic.ListView):
	model = Event
	template_name = 'e_Vent/signUp.html'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Event

class EventCreate(LoginRequiredMixin, CreateView):
	model = Event
	fields = ['title', 'start_time','end_time','location','price','tag','description','href','picture']

class EventUpdate(LoginRequiredMixin, UpdateView):
	model = Event
	fields = ['title', 'start_time','end_time','location','price','tag','description','href','picture']

class EventDelete(LoginRequiredMixin, DeleteView):
	model = Event
	success_url = reverse_lazy('index')

from django.shortcuts import render

# Create your views here.
from .models import Location, Tag, Price, Popularity, Event, User
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
	num_users = User.objects.all().count()
	num_location = Location.objects.all().count()
	popular_events = Event.objects.filter(popularity__gt = 10)

	return render(
		request,
		'index.html',
		context={'events':events,'num_events':num_events,'num_users':num_users,'num_location':num_location,'popular_events':popular_events},

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


from django.core import serializers

class EventDetailView(generic.DetailView):
	model = Event
	template_name = "e_Vent/eventDetails.html"

	# Combining Detail view and retrieve list of event objects
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the events
		context['event_list'] = Event.objects.all()
		return context

	def get_loc(request):
		query_set = Event.objects.values('location')
		list(query_set)
		str =  str(query_set)

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

class YourEventsView(generic.ListView):
	model = Event
	template_name ='e_Vent/profile.html'
	context_object_name = 'event_made'
	# queryset = Event.objects.filter(User__icontains="Tim_Richards")

def eventForm(request):
    return render(request, 'e_vent/eventForm.html')

class EventFormView(generic.ListView):
	model = Event
	template_name = 'e_Vent/form.html'

class LoginView(generic.ListView):
	model = Event
	template_name = 'e_Vent/logIn.html'

class SignupView(generic.ListView):
	model = Event
	template_name = 'e_Vent/signUp.html'
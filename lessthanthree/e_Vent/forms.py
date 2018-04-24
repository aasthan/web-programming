from django import forms
from .models import Event
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class EventForm(forms.Form):
	"""def __init__(self, *args, **kwargs):
	 	#self.profile = user
	 	super(EventForm, self).__init__(*args, **kwargs)
	 	"""
	class Meta:
		model = Event
	title = forms.CharField(label='Name of Event', help_text="The name for the event is...", max_length=100, required=True)
	start_time = forms.DateTimeField(label="Start Time", input_formats=['%Y-%m-%d %H:%M'], help_text="YYYY-MM-DD HH:MM", required=True)
	end_time = forms.TimeField(label="End Time", input_formats=['%Y-%m-%d %H:%M'], help_text="YYYY-MM-DD HH:MM", required=True)
	location = forms.CharField(label="Location", help_text="This event is going to be at...", max_length=100, required=True)
	price = forms.CharField(label='Entry Fee', required=True)
	tag = forms.CharField(label='Categories (Select all that applies)', required=True)
	description = forms.CharField(label='Description', help_text="Write something about my event...", max_length=1000, required=True)
	href = forms.URLField(label='Link to My Event', help_text="My official link is...", max_length=150, required=True)
	picture = forms.ImageField(label='Upload Images', required=True)

	"""def clean_profile(self):
		data = self.profile
		return data"""

	def clean_start_time(self):
		data = self.cleaned_data['start_time']
		if data < datetime.date.today():
			raise ValidationError(_('Invalid date - past date'))
		return data

	def clean_end_time(self):
		befdata = self.cleaned_data['start_time']
		data = self.cleaned_data['end_time']
		if data < datetime.date.today():
			raise ValidationError(_('Invalid date - past date'))
		if data < befdata:
			raise ValidationError(_('Invalid time - end time must be later than start time'))
		return data

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    def __init__(self, *args, **kwargs):
    	super(SignUpForm, self).__init__(*args, **kwargs)
    	for fieldname in ['username', 'password1', 'password2']:
    		self.fields[fieldname].help_text = None

    class Meta:
        model = User
        help_texts = {
            'username': '',
            'password1': '',
            'password2': '',
        }
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


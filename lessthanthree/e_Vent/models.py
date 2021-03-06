from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.conf import settings

### Create your models here.

class Location(models.Model):
    """
    Model representing an event location (e.g. Umass, Mount Holyoke College).
    """
    #An event MUST have a location
    #An event have only ONE location
    name = models.CharField(max_length=500, blank=False, help_text="Enter your event location (e.g. Umass, Mount Holyoke College).")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Tag(models.Model):
    """
    Model representing an event tag (e.g. cultural, sport).
    """
    #An event can have many tags (Many-to-Many relationship)
    #An event MUST have at least one tag
    #Event tag must not exceed 30 characters (we don't want people to put a lengthy tag)
    name = models.CharField(max_length=30, blank=False, help_text="Enter your event tag (e.g. cultural, sport).")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Price(models.Model):
    """
    Model representing an event price price - count by USD$
    """
    #For now we do counting integers
    #An event must have at least 0 $ (Free)
    name = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11,)

    #name = models.PositiveIntegerField(default=0, help_text="Enter your event price (e.g. 0, 5, 10).")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.name)

class Popularity(models.Model):
    """
    Model representing an event popularity - count by number of people
    """
    #For now we do counting integers
    #An event must have at least 0 save
    name = models.IntegerField(default=0, help_text="Popularity of the event")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.name)

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    Model representing a profile.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    name = models.CharField(max_length=100)

    picture = models.ImageField(upload_to = 'imgs/', default = 'imgs/None/no-img.jpg')

    contact = models.CharField(max_length=100, help_text="Enter your email address or phone number.")

    bio = models.TextField(max_length=1000, help_text="Enter a brief description of you/your organization.")

    event = models.ManyToManyField('Event', related_name='+');

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user.username

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

from django.db.models import Count
class Event(models.Model):
    """
    Model representing an event
    """
    title = models.CharField(verbose_name='Name of Event', max_length=100, help_text="The name for the event is...")

    # Foreign Key used because events can only have one user, but users can have multiple events
    profile = models.ForeignKey(User,verbose_name='Organizer', on_delete=models.CASCADE, related_name='+', null=False)

    # A tag can result in many events (Many-to-Many)
    tag = models.ManyToManyField(Tag, verbose_name='Category', help_text="Please specify the category")

    href = models.URLField(verbose_name='Link to the Event',max_length=200, help_text="Link to my event is...")

    # A location can result in many events (Many-to-One)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, help_text="This event is going to be at...")

    description = models.TextField(max_length=1000, help_text="Write something about my event...")

    start_time = models.DateTimeField(verbose_name='Start Time', auto_now=False, auto_now_add=False, help_text="Example: 2017-03-07 06:00:00");
    end_time = models.DateTimeField(verbose_name='End Time', auto_now=False, auto_now_add=False, help_text="Example: 2017-03-07 06:00:00");

    # An event only have one price
    price = models.ForeignKey(Price, verbose_name='Entry Fee', on_delete=models.CASCADE, parent_link=False)

    picture = models.ImageField(verbose_name='Upload Image', upload_to='imgs/', default='imgs/None/no-img.jpg')

    saves = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='saves')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_popu(self):
        """
        Count popularity
        """
        return self.saves.count()

    def get_absolute_url(self):
        """
        Returns the url to access a detail description for this event.
        """
        return reverse('event-details', args=[str(self.id)])

    def get_tag(self):
        '''
        To ensure that only one tag is returned
        '''
        return ''.join([tag.name for tag in self.tag.all()[:1]])

    def display_tag(self):
        """
        Creates a string for the Tag. This is required to display tags in Admin.
        """
        return ', '.join([ tag.name for tag in self.tag.all()[:3] ])

    def display_month(self):
        """
        Display month only (abbr)
        """
        return self.start_time.strftime('%b')

    def display_day(self):
        """
        Display day only
        """
        return self.start_time.strftime('%d')

    def get_loc(self):
        return self.location

    #For save button toggle
    def get_save_url(self):
        return reverse('save', args=[str(self.id)])

    def get_api_save_url(self):
        return reverse('api-save', args=[str(self.id)])

    class Meta:
        ordering = ["start_time"]

    display_tag.short_description = 'Tag'

    popularity = get_popu

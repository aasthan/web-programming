from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.

class Location(models.Model):
    """
    Model representing an event location (e.g. Umass, Mount Holyoke College).
    """
    name = models.CharField(max_length=50, help_text="Enter your event location (e.g. Umass, Mount Holyoke College).")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Tag(models.Model):
    """
    Model representing an event tag (e.g. cultural, sport).
    """
    name = models.CharField(max_length=20, help_text="Enter your event tag (e.g. cultural, sport).")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Price(models.Model):
    """
    Model representing an event price (e.g. $0, $5.5).
    """
    name = models.FloatField(initial='0', help_text="Enter your event price (e.g. 0, 5.5, 10).")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

#TODO 1: needs to modify!
class Popularity(models.Model):
    """
    Model representing an event popularity
    """
    name = models.PositiveIntegerField(required=True, initial='0', help_text="Popularity of the event")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Event(models.Model):
    """
    Model representing an event
    """
    title = models.CharField(required=True, max_length=100)

    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because events can only have one user, but users can have multiple events
    # Users as a string rather than object because it hasn't been declared yet in the file.

    tag = models.ManyToManyField(Tag, required=True, help_text="Select a tag for this book")
    # ManyToManyField used because a tag can contain many events. Events can cover many tags.

    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    description = models.TextField(max_length=1000, required=True, help_text="Enter a brief description of the event")

    start_time = models.DateTimeField(required=True, auto_now_add=True, help_text="Enter the starting date and time of your event");
    end_time = models.DateTimeField(required=True, auto_now_add=True, help_text="Enter the ending date and time of your event");

    price = models.ForeignKey(Price, required= True, on_delete=models.SET_NULL, null=True)

    #TODO 2: Needs to modify
    picture = models.ImageField(upload_to = 'imgs/', default = 'imgs/None/no-img.jpg')

    attendees = models.ManyToManyField('User', on_delete=models.SET_NULL, null=True)

    #TODO 3: Needs to modify to be PositiveIntegerField with the value is the number of attendees
    popularity = models.ForeignKey(Popularity, required= True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a detail description for this event.
        """
        return reverse('event-detail', args=[str(self.id)])

    def display_tag(self):
        """
        Creates a string for the Tag. This is required to display tags in Admin.
        """
        return ', '.join([ tag.name for tag in self.tag.all()[:3] ])

    display_tag.short_description = 'Tag'

class User(models.Model):
    """
    Model representing a user.
    """
    name = models.CharField(max_length=100)

    #TODO 4: Needs to modify
    picture = models.ImageField(upload_to = 'imgs/', default = 'imgs/None/no-img.jpg')

    contact = models.CharField(required=True, max_length=100, help_text="Enter your email address or phone number.")

    bio = models.TextField(max_length=1000, required=True, help_text="Enter a brief description of you/your organization.")


    def get_absolute_url(self):
        """
        Returns the url to access a particular user instance.
        """
        return reverse('user-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

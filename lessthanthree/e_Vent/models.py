from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

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
    name = models.PositiveIntegerField(default=0, help_text="Enter your event price (e.g. 0, 5, 10).")

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
    name = models.PositiveIntegerField(default=0, help_text="Popularity of the event")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.name)

class Event(models.Model):
    """
    Model representing an event
    """
    title = models.CharField(max_length=100)

    # Foreign Key used because events can only have one user, but users can have multiple events
    # Users as a string rather than object because it hasn't been declared yet in the file.
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)

    # A tag can result in many events (Many-to-Many)
    tag = models.ManyToManyField(Tag, help_text="Select a tag for this book")

    # A location can result in many events (Many-to-One)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    description = models.TextField(max_length=1000, help_text="Enter a brief description of the event")

    start_time = models.DateTimeField(auto_now=False, auto_now_add=False, help_text="Enter the starting date and time of your event");
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, help_text="Enter the ending date and time of your event");

    # An event only have one price
    price = models.ForeignKey(Price, on_delete=models.CASCADE, parent_link=False)

    picture = models.ImageField(upload_to = 'imgs/', default = 'imgs/None/no-img.jpg')

    # An event only have one popularity count
    popularity = models.OneToOneField(Popularity, on_delete=models.CASCADE, parent_link=False)


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



    display_tag.short_description = 'Tag'

class User(models.Model):
    """
    Model representing a user.
    """
    name = models.CharField(max_length=100)

    picture = models.ImageField(upload_to = 'imgs/', default = 'imgs/None/no-img.jpg')

    contact = models.CharField(max_length=100, help_text="Enter your email address or phone number.")

    bio = models.TextField(max_length=1000, help_text="Enter a brief description of you/your organization.")


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

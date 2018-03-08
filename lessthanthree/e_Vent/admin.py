from django.contrib import admin

# Register your models here.

from .models import User, Event, Location, Price, Tag, Popularity

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Price)
admin.site.register(Tag)
admin.site.register(Popularity)

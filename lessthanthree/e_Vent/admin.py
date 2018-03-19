from django.contrib import admin

# Register your models here.

from .models import User, Event, Location, Price, Tag, Popularity
'''
Just leave these here, in case we need them later on
'''
# admin.site.register(User)
# admin.site.register(Event)
# admin.site.register(Location)
# admin.site.register(Price)
# admin.site.register(Tag)
# admin.site.register(Popularity)

# Register the Admin classes for Event using the decorator
# ManyToManyField fields aren’t supported in Django list_display, so don't add 'tag' in list_display
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user','location', 'start_time', 'end_time', 'price', 'popularity')
    list_filter = ('location', 'price', 'tag')
    fields = ['title', 'user', 'location','price', 'popularity','tag','description', ('start_time', 'end_time'), 'picture']
    ordering = ('start_time',)

# Register the Admin classes for Popularity using the decorator
@admin.register(Popularity)
class PopularityAdmin(admin.ModelAdmin):
    pass

#TODO - Aasthan
# Register the Admin classes for User using the decorator
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'bio')
    list_filter = ('name', 'contact')

# Register the Admin classes for Location using the decorator
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	pass

# Register the Admin classes for Price using the decorator
@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Tag using the decorator
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

# Register your models here.

from .models import Profile, Event, Location, Price, Tag, Popularity
'''
Just leave these here, in case we need them later on
'''
# admin.site.register(Profile)
# admin.site.register(Event)
# admin.site.register(Location)
# admin.site.register(Price)
# admin.site.register(Tag)
# admin.site.register(Popularity)

# Register the Admin classes for Event using the decorator
# ManyToManyField fields aren’t supported in Django list_display, so don't add 'tag' in list_display
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile','location', 'start_time', 'end_time', 'price', 'popularity')
    list_filter = ('location', 'price', 'tag')
    fields = ['title', 'profile', 'href','location','price', 'popularity','tag','description', ('start_time', 'end_time'), 'picture']
    ordering = ('start_time',)

# Register the Admin classes for Popularity using the decorator
@admin.register(Popularity)
class PopularityAdmin(admin.ModelAdmin):
    pass

#TODO - Aasthan
# Register the Admin classes for Profile using the decorator
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
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

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


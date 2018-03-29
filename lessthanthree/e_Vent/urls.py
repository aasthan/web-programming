from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.indexView, name='index'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-details'),
    path('search/', views.EventSearchView.as_view(), name='search-results'),
    path('eventForm/', views.eventForm, name='event-form'),
    path('profile/',views.YourEventsView.as_view(), name='profile'),
]

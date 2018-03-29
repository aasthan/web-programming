from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.indexView, name='index'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-details'),
    path('search/', views.EventSearchView.as_view(), name='search-results'),
    path('profile/',views.YourEventsView.as_view(), name='profile'),
    path('form/',views.EventFormView.as_view(),name='form'),
    path('browseEvent/',views.browseEventsView, name='browse-Event'),
    path('login/',views.LoginView.as_view(), name = 'login'),
    path('signup/',views.SignupView.as_view(), name = 'signup')
]

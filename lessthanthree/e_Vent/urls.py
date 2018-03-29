from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.EventSearchView.as_view(), name='search'),
    path('', views.indexView, name='index'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-details'),
<<<<<<< HEAD
    path('eventForm/', views.eventForm, name='event-form'),
=======
    path('search/', views.EventSearchView.as_view(), name='search-results'),
>>>>>>> 79f861dda8f4d97ca0a8f79409c53e63e73779d2
    path('profile/',views.YourEventsView.as_view(), name='profile'),
    path('form/',views.EventFormView.as_view(),name='form'),
    path('browseEvent/',views.browseEventsView, name='browse-Event'),
    path('login/',views.LoginView.as_view(), name = 'login'),
    path('signup/',views.SignupView.as_view(), name = 'signup')
]

from django.urls import path
from . import views

urlpatterns = [
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-details'),
    path('', views.IndexView.as_view(), name='index'),
]

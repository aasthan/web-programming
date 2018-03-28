from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-details'),
]

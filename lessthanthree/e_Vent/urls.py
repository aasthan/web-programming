from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-details'),
    path('search/', views.EventSearchView.as_view(), name='search-results'),
]

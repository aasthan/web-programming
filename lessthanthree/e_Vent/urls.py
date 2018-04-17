from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.EventSearchView.as_view(), name='search'),
    path('', views.indexView, name='index'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-details'),
    path('event/<int:pk>/save/', views.PostSaveToggle.as_view(), name='save'),
    path('event/api/<int:pk>/save/', views.PostSaveAPIToggle.as_view(), name='api-save'),
    path('profile/',views.YourEventsView.as_view(), name='profile'),
    #path('profile<int:pk>/your-events',views.YourEventsView.as_view(), name='event_made'),
    path('form/',views.EventFormView.as_view(),name='form'),
    path('browseEvent/',views.browseEventsView, name='browse-Event'),
    path('login/',views.LoginView.as_view(), name = 'login'),
    path('signup/',views.SignupView.as_view(), name = 'signup'),
    path('filterEventByPrice/',views.filterEventByPriceView, name='filter-event-by-price'),
    path('filterEventByLocation/',views.filterEventByLocationView, name='filter-event-by-location'),
    path('filterEventByCategory/',views.filterEventByCategoryView, name='filter-event-by-category'),

    path('event/<int:pk>/update', views.EventUpdate.as_view(), name='event_update'),
    path('event/<int:pk>/delete', views.EventDelete.as_view(), name='event_delete'),

    #path('event/create/', views.EventCreate.as_view(), name='event_create'),
]

urlpatterns += [   
    path('event/create/', views.EventCreate, name='event_create'),
]
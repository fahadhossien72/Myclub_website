from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('event/', views.all_event, name='event'),
    path('create-event/', views.createEvent, name='create-event'),
    path('update-event/<str:pk>/', views.update_event, name='update-event'),
    path('delete-event/<str:pk>/', views.delete_event, name='delete-event'),
    path('create-venue/', views.createVenue, name='venue'),
    path('venue-list/', views.list_venue, name='venue-list'),
    path('show-venue/<str:pk>/', views.show_venue, name='venue-show'),
    path('venue-list/', views.list_venue, name='venue-list'),
    path('search-venue/', views.search_venue, name='search-venue'),
    path('update-venue/<str:pk>/', views.update_venue, name='update-venue'),
    path('delete-venue/<str:pk>/', views.delete_venue, name='delete-venue'),
    path('venue-text/', views.venue_text, name='venue-text'),
    path('venue-csv/', views.venue_csv, name='venue-csv'),
    path('venue-pdf/', views.venue_pdf, name='venue-pdf'),
    
]
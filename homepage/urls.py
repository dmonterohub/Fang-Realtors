from django.urls import path
from . import views

# URL patterns for appropriate paths in homepage app
urlpatterns = [
    path('', views.home, name='homepage-home'),
    path('alllistings/', views.alllistings, name='homepage-alllistings'),
    path('featuredlistings/', views.featuredlistings, name='homepage-featuredlistings'),
    path('searchlistings/', views.searchlistings, name='homepage-searchlistings'),
    path('contacts/', views.contacts, name='homepage-contacts'),
    path('listingtemplate/<str:listing_title>/', views.listingtemplate, name='homepage-listingtemplate')
]
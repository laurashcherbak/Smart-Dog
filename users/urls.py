"""Define URL patterns for users."""

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # Add authentication URL
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
]



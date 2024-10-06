from django.urls import path
from .views import home  # Import the views you create

urlpatterns = [
    path('', home, name='home'),  # Home view for the API
]

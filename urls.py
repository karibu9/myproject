from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),  # The root URL for the hello app
]

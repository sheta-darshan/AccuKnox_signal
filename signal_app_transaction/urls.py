from django.urls import path
from .views import create_model

urlpatterns = [
    path('create/', create_model, name='create_model'),
]
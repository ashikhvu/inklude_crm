from django.urls import path
from . import views

urlpatterns = [
    path('photo_wall', views.photo_wall, name='photo_wall'),
]
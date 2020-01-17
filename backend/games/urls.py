from django.urls import path
from . import views

urlpatterns = [
    path('api/get/games', views.getall, name='games'),
    path('api/get/gamebyid', views.getone, name='gameid'),
]
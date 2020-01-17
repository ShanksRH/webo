from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('api/add/user', views.adduser, name='adduser'),
    path('api/get/user', views.getuser, name='getuser'),
    path('api/saveres', views.save, name='saveres'),
    path('', include('games.urls')),
    path('', include('articles.urls')),
    path('', include('achievements.urls')),
]
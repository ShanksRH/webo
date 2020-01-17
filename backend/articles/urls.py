from django.urls import path
from . import views

urlpatterns = [
    path('api/get/articles', views.getall, name='articles'),
    path('api/get/articlebyid', views.getone, name='articleid'),
]
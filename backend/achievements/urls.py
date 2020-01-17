from django.urls import path
from . import views

urlpatterns = [
    path('api/get/achieves', views.getall, name='achieves'),
    path('api/get/achievebyid', views.getone, name='achieveid'),
]
from django.urls import path
from .views import *
from django.views.generic.base import TemplateView 


urlpatterns = [
    path('',home,name='home'),
    path('register-user/',registerUser,name='register-user'),
    path('room/<str:pk>/',room,name='room'),
    path('create-room/',createRoom,name='create-room'), 

]

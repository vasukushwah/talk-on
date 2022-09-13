from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('room/<str:pk>/',room,name='room'),
]

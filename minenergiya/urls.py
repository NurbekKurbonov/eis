
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name='home'),
    path('tahlil', views.tahlil, name='tahlil'), 
]
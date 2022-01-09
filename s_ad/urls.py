
from django.urls import path
from . import views

urlpatterns = [
    path('', views.kirishP, name='kirishP'),  
    path('addkir', views.addkir, name='addkir'),
    
    path('icons', views.icons, name='icons'),
]
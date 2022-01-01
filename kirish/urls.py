
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginP, name='loginP'),
    path('register', views.registerP, name='register'),
    path('xato404', views.xato404, name='xato404'),
    path('xato500', views.xato500, name='xato500'),
    path('reset', views.resetpas, name='reset'),
    
    path('', views.kirish, name='kirish'),
]


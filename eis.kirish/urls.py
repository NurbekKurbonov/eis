
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginP, name='loginP'),
    path('register', views.registerP, name='register'),
    path('xato500', views.xato500, name='xato500'),
    path('reset', views.resetpas, name='reset'),
    path('savolnoma', views.savol, name='savolnoma'),
    
    #kirish url *****************************************
    path('', views.kirish, {'pagename':''}, name='kirish'),
    path('contact', views.contact, name='contact'),
    path('<str:pagename>', views.kirish, name='index'),   
    
]
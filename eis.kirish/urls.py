
from django.urls import path
from . import views
from .views import registerP, UsernameValidationView
import json
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('login', views.loginP, name='loginP'),
    
    path('register', registerP.as_view(), name='register'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    
    
    path('xato500', views.xato500, name='xato500'),
    path('reset', views.resetpas, name='reset'),
    path('savolnoma', views.savol, name='savolnoma'),
    
    #kirish url *****************************************
    path('', views.kirish, {'pagename':''}, name='kirish'),
    path('contact', views.contact, name='contact'),
    path('<str:pagename>', views.kirish, name='index'),   
    
]
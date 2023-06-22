from django.urls import path
from . import views
from .views import registerP, UsernameValidationView, EmailValidationView, StirValidationView, passwordValidationView, VerificationView, loginP, LogoutView, resetpas
from django.views.decorators.csrf import csrf_exempt

from django.contrib import auth
from django.utils import timezone

urlpatterns = [
    path('register/<str:til>', registerP.as_view(), name='register'),
    path('loginP/<str:til>', loginP.as_view(), name='loginP'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name='validate_email'),
    path('validate-stir', csrf_exempt(StirValidationView.as_view()),
         name='validate-stir'),
    path('validate-password', csrf_exempt(passwordValidationView.as_view()),
         name='validate-password'), 
    path('activate/<uidb64>/<token>/<str:til>', VerificationView.as_view(), name="activate"),    
     
     path('davlatadd', views.davlatadd, name='davlatadd'),
     path('viladd', views.viladd, name='viladd'),
     
    path('logout', LogoutView.as_view(), name="logout"),
    
    path('reset', resetpas.as_view(), name='reset'),
    path('savolnoma', views.savol, name='savolnoma'),
    
    #kirish url *****************************************
    path('', views.kirish, {'pagename':''}, name='kirish'),
    path('<str:til>', views.kirish_til, {'pagename':''}, name='kirish_til'),
    
    path('contact', views.contact, name='contact'),
    path('<str:pagename>', views.kirish, name='index'),   
    
    path('404', views.view404, name='view404'),

   
    
]
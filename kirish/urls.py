from django.urls import path
from . import views
from .views import registerP, UsernameValidationView, EmailValidationView, StirValidationView, passwordValidationView, VerificationView
from django.views.decorators.csrf import csrf_exempt

from django.contrib import auth

urlpatterns = [
    path('login', views.loginP, name='loginP'),
    
    #registratsya url
    path('register', registerP.as_view(), name='register'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name='validate_email'),
    
    path('validate-stir', csrf_exempt(StirValidationView.as_view()),
         name='validate-stir'),
    path('validate-password', csrf_exempt(passwordValidationView.as_view()),
         name='validate-password'),    
    
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),
    
    path('reset', views.resetpas, name='reset'),
    path('savolnoma', views.savol, name='savolnoma'),
    
    #kirish url *****************************************
    path('', views.kirish, {'pagename':''}, name='kirish'),
    path('contact', views.contact, name='contact'),
    path('<str:pagename>', views.kirish, name='index'),   
    
]
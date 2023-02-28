
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.bosh_sahifa, name='bosh_sahifa_tarjimon'),    
    path('tarjima/<str:til>', views.tarjima, name='tarjima'),
]



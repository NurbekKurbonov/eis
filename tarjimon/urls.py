
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.bosh_sahifa, name='bosh_sahifa_tarjimon'),    
    path('tarjima/<str:til>', views.tarjima, name='tarjima'),
    path('tarjimoni/<int:id>/<str:til>', views.tarjimon, name='tarjimoni'),
    path('addtil', views.addtil, name='addtil'),
    path('edittil/<int:id>', views.edittil, name='edittil'),
    path('deltil/<int:id>', views.deltil, name='deltil'),
    path('deltarjima/<int:id>', views.deltarjima, name='deltarjima'),
]
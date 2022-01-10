
from django.urls import path
from . import views

urlpatterns = [
    path('', views.kirishP, name='kirishP'),  
    path('addkir', views.addkir, name='addkir'),
    path('editkir/<int:id>', views.editkir, name='editkir'),
    path('delkir/<int:id>', views.delkir, name='delkir'),
    
    path('davlat', views.davlat, name='davlat'),
    
    path('icons', views.icons, name='icons'),
]
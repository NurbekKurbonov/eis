
from django.urls import path
from . import views

urlpatterns = [
    path('icons', views.icons, name='icons'),
    
    path('', views.kirishP, name='kirishP'), 
     
    path('addkir', views.addkir, name='addkir'),
    path('editkir/<int:id>', views.editkir, name='editkir'),
    path('delkir/<int:id>', views.delkir, name='delkir'),
    
    #*******DAVLAT*********************************************
    path('davlat', views.davlat, name='davlat'),
    path('adddavlat', views.adddavlat, name='adddavlat'),
    path('editdavlat/<int:id>', views.editdavlat, name='editdavlat'),
    path('deldavlat/<int:id>', views.deldavlat, name='deldavlat'),
    
    #*******Viloyat*********************************************
    path('viloyat', views.viloyat, name='viloyat'),
    path('addviloyat', views.addviloyat, name='addviloyat'),
    path('editviloyat/<int:id>', views.editviloyat, name='editviloyat'),
    path('delviloyat/<int:id>', views.delviloyat, name='delviloyat'),
    
    #*******Viloyat*********************************************
    path('tuman', views.tuman, name='tuman'),
    path('addtuman', views.addtuman, name='addtuman'),
    path('edittuman/<int:id>', views.edittuman, name='edittuman'),
    path('deltuman/<int:id>', views.deltuman, name='deltuman'),    
    
    #*******OFTUM*********************************************
    path('iftums', views.iftums, name='iftums'),
    path('addiftums', views.addiftums, name='addiftums'),
    path('editiftums/<int:id>', views.editiftums, name='editiftums'),
    path('deliftums/<int:id>', views.deliftums, name='deliftums'), 
    
    #*******DBIBT*********************************************
    path('dbibt', views.dbibt, name='dbibt'),
    path('adddbibt', views.adddbibt, name='adddbibt'),
    path('editdbibt/<int:id>', views.editdbibt, name='editdbibt'),
    path('deldbibt/<int:id>', views.deldbibt, name='deldbibt'), 
    
    #*******thst*********************************************
    path('thst', views.thst, name='thst'),
    path('addthst', views.addthst, name='addthst'),
    path('editthst/<int:id>', views.editthst, name='editthst'),
    path('delthst/<int:id>', views.delthst, name='delthst'), 
    
    #*******Birliklar*********************************************
    path('birlik', views.birlik, name='birlik'),
    path('addbirlik', views.addbirlik, name='addbirlik'),
    path('editbirlik/<int:id>', views.editbirlik, name='editbirlik'),
    path('delbirlik/<int:id>', views.delbirlik, name='delbirlik'), 
    
    #*******Resurs*********************************************
    path('resurs', views.resurs, name='resurs'),
    path('addresurs', views.addresurs, name='addresurs'),
    path('editresurs/<int:id>', views.editresurs, name='editresurs'),
    path('delresurs/<int:id>', views.delresurs, name='delresurs'), 
    
    #******Foydalanuvchi sozlama****************************
    path('usersozlama', views.usersozlama, name='usersozlama'),
    
    #*******Resurs*********************************************
    path('valyuta', views.valyuta, name='valyuta'),
    path('addvalyuta', views.addvalyuta, name='addvalyuta'),
    path('editvalyuta/<int:id>', views.editvalyuta, name='editvalyuta'),
    path('savevalyuta/<int:id>', views.savevalyuta, name='savevalyuta'),
    path('delvalyuta/<int:id>', views.delvalyuta, name='delvalyuta'),
]

from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name='home'), 
    
    path('asosiyset/<int:id>', views.asosiyset, name='asosiyset'),  
    path('mich', views.mich, name='mich'),      
    path('ist', views.ist, name='ist'),
    path('sot', views.sot, name='sot'),  
    
    path('add', views.add, name='add'),
    
    path('davr', views.davr, name='davr'),
    path('adddavr', views.adddavr, name='adddavr'),
    path('checkdavr/<int:id>', views.checkdavr, name='checkdavr'),
    
    path('hisobot', views.hisobot, name='hisobot'),
    path('addhisobot', views.addhisobot, name='addhisobot'),
    path('addichresforhis', views.addichresforhis, name='addichresforhis'),
    
    path('delhis/<int:id>', views.delhis, name='delhis'),
    path('result_his', views.result_his, name='result_his'),
    #path('checkdavr/<int:id>', views.checkdavr, name='checkdavr'),
]

from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name='home'), 
    
    path('asosiyset', views.asosiyset, name='asosiyset'),  
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
    
    path('result_his/<int:id>/<str:tur>/<str:birl>', views.result_his, name='result_his'),
    
    #_____________prognoz______________________
    path('pronoz', views.prognoz, name='prognoz'),   
    path('addprognoz', views.addprognoz, name='addprognoz'),
    path('resultprognoz', views.resultprognoz, name='resultprognoz'),
    
    #_____________Me'yorlash______________________
    path('norm', views.norm, name='norm'),   
    path('addnorm', views.addnorm, name='addnorm'),
    path('resultnorm', views.resultnorm, name='resultnorm'),
    
    #_____________Balans______________________
    path('balans', views.balans, name='balans'),
    path('addbalans', views.addbalans, name='addbalans'),
    path('resultbalans', views.resultbalans, name='resultbalans'),
    
]
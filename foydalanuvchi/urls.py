
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [    
    path('', views.home,  name='home'), 
    
    path('asosiyset', views.asosiyset, name='asosiyset'),  
    path('mich', views.mich, name='mich'),      
    path('ist', views.ist, name='ist'),
    path('sot', views.sot, name='sot'),  
    
    path('addichres/<str:bol>', views.addichres, name='addichres'),  
    
    path('add', views.add, name='add'),
    
    #**********shartnomaviy miqdorlar*******************
    path('reja', views.reja, name='reja'),
    path('addreja', views.addreja, name='addreja'),
    path('checkreja/<int:id>', views.checkreja, name='checkreja'),
    
    #**********davriy ma'lumotlar**********************
    path('davr', views.davr, name='davr'),
    path('adddavr', views.adddavr, name='adddavr'),
    path('checkdavr/<int:id>', views.checkdavr, name='checkdavr'),
    
    path('vvp', views.vvp, name='vvp'),
    path('addvvp', views.addvvp, name='addvvp'),

    path('hisobot', views.hisobot, name='hisobot'),
    path('addhisobot', views.addhisobot, name='addhisobot'),
    path('addichresforhis', views.addichresforhis, name='addichresforhis'),
    
    path('delhis/<int:id>', views.delhis, name='delhis'),    
    path('result_his/<int:id>/<str:tur>/<str:birl>', views.result_his, name='result_his'),
    path('zoom_plus/<int:id>/<str:tur>/<str:birl>', views.zoom_plus, name='zoom_plus'),
    
    #_______________Texnik tadbir__________________________________
    path('ftadbir', views.tadbir, name='ftadbir'),
    path('addtexniktadbir/<str:id>', views.addtexniktadbir, name='addtexniktadbir'),
    path('addttt', views.addttt, name='addttt'),
    path('delttt/<int:id>/<int:T_ID>', views.delttt, name='delttt'),  
    path('addt_umumiy', views.addt_umumiy, name='addt_umumiy'),
    path('tttsave/<str:T_ID>/<int:id>', views.tttsave, name='tttsave'),
    path('t_umumiysave/<str:T_ID>/<int:id>', views.t_umumiysave, name='t_umumiysave'),
    path('deltexniktadbir/<int:id>', views.deltexniktadbir, name='deltexniktadbir'),
    path('fakttadbir/<int:id>', views.fakttadbir, name='fakttadbir'),
    path('faktsave/<int:id1>/<int:id2>', views.faktsave, name='faktsave'),
    path('faktedit/<int:id1>/<int:id2>', views.faktedit, name='faktedit'),

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

    #_____________Samaradorlik______________________
    path('samaradorlik', views.ensam, name='samaradorlik'),
    path('changesam', views.changesam, name='changesam'),
    #path('resultbalans', views.resultbalans, name='resultbalans'),

    #**************SIFAT**************************************************
    path('hisoblagichlar', views.hisoblagichlar, name='hisoblagichlar'),
    path('tahrir/<int:id>', views.tahrir, name='tahrir'),
    path('editpas', csrf_exempt(views.editpas.as_view()),
         name='editpas'), 
    path('editmail', csrf_exempt(views.editmail.as_view()),
         name='editmail'),
         
     path('fxabarlar', views.fxabarlar, name='fxabarlar'),
     path('fxabaropen', views.fxabaropen, name='fxabaropen'),
     path('addressor/<int:id>', views.addressor, name='addressor'),

     path('delres/<str:bol>/<int:id>', views.delres, name='delres'),

     path('opros', views.opros, name='opros'),

     path('qtemqurilma', views.qtemqurilma, name='qtemqurilma'),
     path('qtemholats', views.qtemholats, name='qtemholats'),
     path('addqtemholat', views.addqtemholat, name='addqtemholat'),
     path('saveqtemholat/<int:id>', views.saveqtemholat, name='saveqtemholat'),
     path('editqtemholat/<int:id>', views.editqtemholat, name='editqtemholat'),
     path('delqtemholat/<int:id>', views.delqtemholat, name='delqtemholat'),
]

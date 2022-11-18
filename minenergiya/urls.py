
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name='wbonehome'),
    path('korxonalar', views.korxonalar, name='korxonalar'), 

    #****************I jadval*******************************
    path('I_jadval', views.I_result, name='I_jadval'), 
    path('I_add', views.I_add, name='I_add'), 
    path('I_result', views.I_result, name='I_result'), 

    #****************II jadval*******************************
    path('II_result', views.II_result, name='II_result'), 

    #****************II jadval*******************************
    path('III_result', views.III_result, name='III_result'), 

    #****************Texnik tadbirlar*******************************
    path('t_umumiy', views.t_umumiy, name='t_umumiy'), 

    #****************Texnik tadbirlar*******************************
    path('ensamkor', views.ensamkor, name='ensamkor'), 
    path('addbyshablon/<str:bolim>', views.addbyshablon, name='addbyshablon'), 
    path('addensamkor/<str:E_ID>', views.addensamkor, name='addensamkor'), 
    
    path('fqr_show/<str:E_ID>', views.fqr_show, name='fqr_show'), 
    path('delfaqirshow/<int:id>/<str:E_ID>', views.delfaqirshow, name='delfaqirshow'), 
    
    path('ensamkor_result/<int:id>', views.ensamkor_result, name='ensamkor_result'), 

    path('addfiltrres/<str:E_ID>', views.addfiltrres, name='addfiltrres'), 
    path('delfiltrres/<int:id>/<str:E_ID>', views.delfiltrres, name='delfiltrres'),
    
    path('addguruh/<str:E_ID>', views.addguruh, name='addguruh'), 
    path('savenameguruh/<int:id>/<str:E_ID>', views.savenameguruh, name='savenameguruh'), 
    path('addfqrtoguruh/<int:id1>/<int:id2>/<str:E_ID>', views.addfqrtoguruh, name='addfqrtoguruh'), 
    path('delfqrtoguruh/<int:id1>/<int:id2>/<str:E_ID>', views.delfqrtoguruh, name='delfqrtoguruh'), 
    path('delgr/<int:id>/<str:E_ID>', views.delgr, name='delgr'),
    
    path('addtur/<str:E_ID>', views.addtur, name='addtur'), 
    path('deltur/<int:id>/<str:E_ID>', views.deltur, name='deltur'), 
    path('addklassifikator/<str:E_ID>', views.addklassifikator, name='addklassifikator'), 
    path('delklassifikator/<int:id>/<str:E_ID>', views.delklassifikator, name='delklassifikator'),
    
    path('delensamfilter/<int:id>/<str:E_ID>', views.delensamfilter, name='delensamfilter'),
    
] 

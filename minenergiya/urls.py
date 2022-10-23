
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
    path('addensamkor', views.addensamkor, name='addensamkor'), 
    
    path('fqr_show', views.fqr_show, name='fqr_show'), 
    path('delfaqirshow/<int:id>', views.delfaqirshow, name='delfaqirshow'), 
    
    path('ensamkor_result', views.ensamkor_result, name='ensamkor_result'), 

    path('addfiltrres', views.addfiltrres, name='addfiltrres'), 
    path('delfiltrres/<int:id>', views.delfiltrres, name='delfiltrres'),
    
    path('addguruh', views.addguruh, name='addguruh'), 
    path('savenameguruh/<int:id>', views.savenameguruh, name='savenameguruh'), 
    path('addfqrtoguruh/<int:id1>/<int:id2>', views.addfqrtoguruh, name='addfqrtoguruh'), 
    path('delfqrtoguruh/<int:id1>/<int:id2>', views.delfqrtoguruh, name='delfqrtoguruh'), 
    path('delgr/<int:id>', views.delgr, name='delgr'),
    
    path('addtur', views.addtur, name='addtur'), 
    path('deltur/<int:id>', views.deltur, name='deltur'), 
    path('addklassifikator', views.addklassifikator, name='addklassifikator'), 
    path('delklassifikator/<int:id>', views.delklassifikator, name='delklassifikator'),

] 

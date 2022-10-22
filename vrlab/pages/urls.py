from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),  
  path('kitob/<int:id>', views.kitob, name='kitob'),
  path('theme/<int:id>', views.theme, name='theme'),
  
  path('test', views.test, name='test'),
  
  path('vrlab', views.vrlab, name='vrlab'),
  
  path('lab1', views.lab1, name='lab1'),
  path('lab1_result', views.lab1_result, name='lab1_result'),

  path('lab2', views.lab2, name='lab2'),  

  path('lab3', views.lab3, name='lab3'),

]
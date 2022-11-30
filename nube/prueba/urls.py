from django.contrib import admin
from django.urls import path
from .views import*
import re
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from .views import *



urlpatterns = [
    #CRUD DE BASE 
    path('base/', listar,name="base"),
    #CRUD DE PRUEBA
    path('listar/',listar,name="listar"),
    path('crear/', carrocrear, name='crear'),
    path('eliminar/<int:id>',eliminar,name='eliminar'),
    path('actualizar/<int:id>',actualizar,name='actualizar'),
    #CRUD DE PIZZA
    path('listarpizza/', listarpizza, name="listarpizza"),
    path('crearpizza/', crearpizza, name='crearpizza'),
    path('eliminarpizza/<int:id>', eliminarpizza, name='eliminarpizza'),
    path('actualizarpizza/<int:id>', actualizarpizza, name='actualizarpizza'),
    #CRUD DE PASTELES
    path('listarpostre/', listarpostre, name="listarpostre"),
    path('crearpostre/', crearpostre, name='crearpostre'),
    path('eliminarpostre/<int:id>', eliminarpostre, name='eliminarpizza'),
    path('actualizarpostre/<int:id>', actualizarpostre, name='actualizarpostre'),
]
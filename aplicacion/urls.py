from django.urls import path, include 
from .views import *
urlpatterns = [
    path('', index, name="inicio" ),

#Visualizar BD
    path('bodegas/', bodegas, name="bodegas" ),
    path('departamentos/', departamentos, name="Departamentos" ),
    path('estacionamientos/', estacionamientos, name="Estacionamientos" ),
    path('terrenos/', terrenos, name="Terrenos" ),


#formularios
    path('dept_form/', dept_form, name="dept_form" ),
    path('bodega_form/', bodega_form, name="bodega_form" ),
    path('terrenos_form/', terrenos_form, name="terrenos_form" ),
    path('est_form/', est_form, name="est_form" ),


#busqueda
    path('buscar_dpto/', buscardpto, name="buscar_dpto" ),
    path('buscar2/', buscar2, name="buscar2" ),
]
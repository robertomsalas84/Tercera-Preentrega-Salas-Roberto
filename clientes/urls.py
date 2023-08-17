from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('cliente/', cliente, name="cliente"),
    path('producto_form2/', productoForm2, name="producto"),
    path('sucursal_form2/', sucursalForm2, name="sucursal"),
    path('cliente_form/', clienteForm, name="cliente_form"),
    path('cliente_form2/', clienteForm2, name="cliente_form2"),
    path('buscar_cliente/', buscarCliente, name="buscar_cliente"),
    path('buscar2/', buscar2, name="buscar2"),
    path('producto_form/', productoForm, name="producto_form"),
    path('sucursal_form/', sucursalForm, name="sucursal_form")


]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('new_cliente/', views.new_cliente, name='new_cliente'),
    path('edit_cliente/<int:id_cliente>/', views.edit_cliente, name='edit_cliente'),    
]
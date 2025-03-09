from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('search_clientes/', views.search_clientes, name='search_clientes'),
    path('new_cliente/', views.new_cliente, name='new_cliente'),
    path('edit_cliente/<int:id_cliente>/', views.edit_cliente, name='edit_cliente'),
    path('fornecedores/', views.fornecedores, name='fornecedores'),
    path('search_fornecedores/', views.search_fornecedores, name='search_fornecedores'),
    path('new_fornecedor/', views.new_fornecedor, name='new_fornecedor'),
    path('edit_fornecedor/<int:id_fornecedor>/', views.edit_fornecedor, name='edit_fornecedor'),    
]
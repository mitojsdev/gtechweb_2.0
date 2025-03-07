from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página vendas realizadas
    path('venda', views.venda, name='venda'),
    path('new_venda', views.new_venda, name='new_venda'),
    path('get_preco_custo/<int:produto_id>', views.get_preco_custo, name='get_preco_custo'),       
]
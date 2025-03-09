from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página tipos de produtos
    path('tipo_produto', views.tipo_produto, name='tipo_produto'),
    path('new_tipo_produto', views.new_tipo_produto, name='new_tipo_produto'),
    path('edit_tipo_produto/<int:tipo_id>', views.edit_tipo_produto, name='edit_tipo_produto'),
    path('produto', views.produto, name='produto'),
    path('search_produto', views.search_produto, name='search_produto'),
    path('new_produto', views.new_produto, name='new_produto'),
    path('edit_produto/<int:produto_id>', views.edit_produto, name='edit_produto'),    
]
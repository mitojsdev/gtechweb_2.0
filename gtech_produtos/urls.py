from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página tipos de produtos
    path('tipo_produto', views.tipo_produto, name='tipo_produto'),
    path('new_tipo_produto', views.new_tipo_produto, name='new_tipo_produto'),
    path('edit_tipo_produto/<int:tipo_id>', views.edit_tipo_produto, name='edit_tipo_produto'),    
]
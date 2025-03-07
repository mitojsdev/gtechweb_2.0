from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página vendas realizadas
    path('venda', views.venda, name='venda'),        
]
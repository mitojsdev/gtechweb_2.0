from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página vendas realizadas    
    path('inicio/', views.dashboard, name='inicio'),    
]
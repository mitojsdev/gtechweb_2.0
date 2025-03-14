from django.urls import path
from .views import *


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('usuarios/', usuarios,name='usuarios'),
    path('new_user/',new_user, name='new_user'),
    path('edit_user/<int:user_id>', edit_user, name='edit_user'),
    path('grupos/', grupos, name='grupos'),
    path('definir_senha/<int:user_id>/', definir_senha, name='definir_senha')
]
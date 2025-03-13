from django.urls import path
from .views import *
from .views import new_user

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('new_user/',new_user, name='new_user'),
    path('definir_senha/<int:user_id>/', definir_senha, name='definir_senha')
]
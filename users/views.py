from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
import random, string
from django.core.mail import send_mail

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


def new_user(request):
    """Página de cadastro de usuarios."""

    groups = Group.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        group_name = request.POST.get('group', None)  # Nome do grupo (opcional)

        # Gerar senha temporária
        temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        # Criar usuário sem senha definida
        user = User.objects.create_user(username=username, email=email, password=temp_password)
        user.is_active = False  # Bloqueia até definir senha
        user.save()

        # Adicionar ao grupo, se informado
        if group_name:
            try:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
            except Group.DoesNotExist:
                messages.warning(request, "Grupo não encontrado.")

        # Enviar e-mail para definir senha
        send_mail(
            'Cadastro no Gtech Web Control',
            f'Olá, {username}! Você foi cadastrado no sistema.\n\nAcesse: http://127.0.0.1:8000/users/definir-senha/{user.pk}/\n\nUse esta senha temporária: {temp_password}\n\nApós login, altere sua senha.',
            'amiltonsogm@gmail.com',  # E-mail do sistema
            [email],
            fail_silently=False,
        )

        messages.success(request, f'Usuário {username} cadastrado com sucesso!')
        return redirect('inicio')

    context = {'groups': groups}
    return render(request, 'users/new_user.html', context)

def definir_senha(request, user_id):
    User = get_user_model()
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            user.is_active = True  # Ativar o usuário
            form.save()
            messages.success(request, "Senha definida com sucesso! Faça login.")
            return redirect('login')
    else:
        form = SetPasswordForm(user)
    
    return render(request, 'users/definir_senha.html', {'form':form})
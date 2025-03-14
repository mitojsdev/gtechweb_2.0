from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import random, string
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, user_passes_test
from gtechwebs.views import verifica_permissao

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


@login_required
@user_passes_test(verifica_permissao('auth', 'view_user'),login_url='acesso_negado')
def usuarios(request):
    """Página de usuários."""
    users = User.objects.all()
    context = {
        'usuarios': users
    }
    return render(request, 'users/usuarios.html', context)

@login_required
@user_passes_test(verifica_permissao('auth', 'add_user'),login_url='acesso_negado')
def new_user(request):
    """Página de cadastro de usuarios."""

    groups = Group.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        group_name = request.POST.get('group', None)  # Nome do grupo (opcional)
        print(f"Grupo selecionado pelo usuário: {group_name}")

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
                print(group)
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

@login_required
@user_passes_test(verifica_permissao('auth', 'change_user'),login_url='acesso_negado')
def edit_user(request, user_id):
    """Página de edição de usuários."""
    usuario = get_object_or_404(User, id=user_id)
    grupos = Group.objects.all()  # Obtém todos os grupos disponíveis

    if request.method == "POST":
        usuario.username = request.POST["username"]
        usuario.email = request.POST["email"]
        group_name = request.POST.get("group", None)

        # Atualiza o grupo do usuário
        if group_name:
            novo_grupo = Group.objects.get(name=group_name)
            usuario.groups.clear()  # Remove o usuário de todos os grupos antes de adicionar ao novo
            usuario.groups.add(novo_grupo)

        usuario.save()
        messages.success(request, "Usuário atualizado com sucesso!")
        return redirect("usuarios")  # Redireciona para a lista de usuários

    context = {
        "usuario": usuario,
        "grupos": grupos
    }
    return render(request, "users/edit_user.html", context)

@login_required
@user_passes_test(verifica_permissao('auth', 'view_user'),login_url='acesso_negado')
def grupos(request):
    """Página de exibição de grupos e permissões"""
    grupos = Group.objects.all()
    context = {'grupos': grupos}
    return render(request,'users/grupos.html', context)


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
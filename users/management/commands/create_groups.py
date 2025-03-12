from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Cria grupos de usuários'

    def handle(self, *args, **kwargs):
        grupos = {
            'Administrador': ['add_user', 'change_user', 'delete_user', 'view_user'],
            'Vendedor': ['add_venda', 'view_venda'],
            'Estoquista': ['add_produto', 'change_produto', 'view_produto'],
        }

        for nome, permissoes in grupos.items():
            grupo, criado = Group.objects.get_or_create(name=nome)
            if criado:
                for perm_codename in permissoes:
                    perm = Permission.objects.filter(codename=perm_codename).first()
                    if perm:
                        grupo.permissions.add(perm)
                    else:
                        print(f'⚠️ Atenção: Permissão "{perm_codename}" não encontrada!')
                print(f'✅ Grupo {nome} criado com permissões: {permissoes}')
            else:
                print(f'ℹ️ Grupo {nome} já existe.')

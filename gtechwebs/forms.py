from django import forms
from .models import TbCliente, TbFornecedor

class ClienteForm(forms.ModelForm):
    class Meta:
        model = TbCliente
        fields = ['nome', 'telefone', 'email']
        labels = {'nome': 'Nome', 'telefone': 'Telefone', 'email': 'E-mail'}
        widgets = {
            'nome': forms.TextInput(attrs={'size': '30'}),  # Define o tamanho do input
            'telefone': forms.TextInput(attrs={'size': '15'}),
            'email': forms.EmailInput(attrs={'size': '30'}),
        }

class FornecedorForm(forms.ModelForm):
    TIPO_EMPRESA_CHOICES = [
        ('fisica', 'Física'),
        ('digital', 'Digital'),
        ('outros', 'Outros'),
    ]

    tipo_empresa = forms.ChoiceField(
        choices=TIPO_EMPRESA_CHOICES,  # Define as opções disponíveis
        widget=forms.Select(),  # Usa um widget de seleção (dropdown)
        label="Tipo de Empresa"  # Define um rótulo opcional
    )

    class Meta:
        model = TbFornecedor  # Substitua pelo nome real do seu modelo
        fields = ['nome_empresa', 'tipo_empresa']
        widgets = {
            'nome_empresa': forms.TextInput(attrs={'size': '30'}),
        }

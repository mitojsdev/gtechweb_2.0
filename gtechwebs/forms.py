from django import forms
from .models import TbCliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = TbCliente
        fields = ['nome', 'telefone']
        labels = {'nome': 'Nome', 'telefone': 'Telefone'}
        widgets = {
            'nome': forms.TextInput(attrs={'size': '30'}),  # Define o tamanho do input
            'telefone': forms.TextInput(attrs={'size': '15'}),
        }
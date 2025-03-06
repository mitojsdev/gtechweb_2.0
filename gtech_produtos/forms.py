from django import forms
from gtechwebs.models import TbTipoProduto

class TipoProdutoForm(forms.ModelForm):
    class Meta:
        model = TbTipoProduto
        fields = ['descricao', 'margem']
        labels = {'descricao': 'Descrição', 'margem': 'Margem'}
        widgets = {'descricao': forms.TextInput(attrs={'class': 'form-control'}),
                   'margem': forms.NumberInput(attrs={'class': 'form-control'})}
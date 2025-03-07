from django import forms
from gtechwebs.models import TbVenda

class VendaForm(forms.ModelForm):
    class Meta:
        model = TbVenda
        fields = ['data', 'id_cliente', 'id_produto','quantidade', 'preco_venda', 'lucro']
        labels = {'data': 'Data da Venda', 'id_cliente': 'Cliente', 'id_produto': 'Produto', 'quantidade': 'Quantidade', 'preco_venda': 'Preço de Venda', 'lucro': 'Lucro'}
        widgets = {'data': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
                   'id_cliente': forms.Select(attrs={'class': 'form-control', 'id': 'id_cliente'}),                   
                   'id_produto': forms.Select(attrs={'class': 'form-control', 'id': 'id_produto'}),
                   'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_quantidade'}),
                   'preco_venda': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_preco_venda'}),
                   'lucro': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'id': 'id_lucro'})}
                    
        

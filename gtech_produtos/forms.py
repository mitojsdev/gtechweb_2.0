from django import forms
from gtechwebs.models import TbTipoProduto, TbProduto

class TipoProdutoForm(forms.ModelForm):
    class Meta:
        model = TbTipoProduto
        fields = ['descricao', 'margem']
        labels = {'descricao': 'Descrição', 'margem': 'Margem'}
        widgets = {'descricao': forms.TextInput(attrs={'class': 'form-control'}),
                   'margem': forms.NumberInput(attrs={'class': 'form-control'})}
        
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = TbProduto
        fields = ['nome', 'preco_custo', 'tipo_produto', 'fabricante', 'marca', 'cor', 'id_fornecedor', 'estoque', 'imagem']
        labels = {'nome': 'Nome', 'preco_custo': 'Preço de Custo', 'tipo_produto': 'Tipo de Produto', 'fabricante': 'Fabricante', 'marca': 'Marca', 'cor': 'Cor', 'id_fornecedor': 'Fornecedor', 'estoque': 'Estoque', 'imagem': 'Imagem'}
        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control'}),
                   'preco_custo': forms.NumberInput(attrs={'class': 'form-control'}),
                   'tipo_produto': forms.Select(attrs={'class': 'form-control'}),
                   'fabricante': forms.TextInput(attrs={'class': 'form-control'}),
                   'marca': forms.TextInput(attrs={'class': 'form-control'}),
                   'cor': forms.TextInput(attrs={'class': 'form-control'}),
                   'id_fornecedor': forms.Select(attrs={'class': 'form-control'}),
                   'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
                   'imagem': forms.TextInput(attrs={'class': 'form-control'})}
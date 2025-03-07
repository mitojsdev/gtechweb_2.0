from django import forms
from gtechwebs.models import TbTipoProduto, TbProduto

class TipoProdutoForm(forms.ModelForm):
    class Meta:
        model = TbTipoProduto
        fields = ['descricao', 'margem']
        labels = {'descricao': 'Descrição', 'margem': 'Margem'}
        widgets = {'descricao': forms.TextInput(attrs={'class': 'form-control'}),
                   'margem': forms.NumberInput(attrs={'class': 'form-control'})}
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.descricao = instance.descricao.upper()  # Convertendo para uppercase

        if commit:
            instance.save()
        return instance
        
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
                   'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'})}
        
    def save(self, commit=True):
        instance = super().save(commit=False)

        # Convertendo os campos de texto para uppercase
        instance.nome = instance.nome.upper()
        instance.fabricante = instance.fabricante.upper()
        instance.marca = instance.marca.upper()
        instance.cor = instance.cor.upper()

        if commit:
            instance.save()
        return instance
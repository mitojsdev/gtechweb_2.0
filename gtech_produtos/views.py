from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from gtechwebs.models import TbTipoProduto
from .forms import TipoProdutoForm
# Create your views here.

def tipo_produto(request):
    """Página de tipos de produtos."""
    tipos = TbTipoProduto.objects.all()
    context = {
        'tipos': tipos
    }
    return render(request, 'gtech_produtos/tipo_produto.html', context)

def new_tipo_produto(request):
    """Adiciona um novo tipo de produto."""
    if request.method != 'POST':
        # Dados não submetidos; cria um formulário em branco.
        form = TipoProdutoForm()
    else:
        # Dados submetidos; processa os dados.
        form = TipoProdutoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tipo_produto'))
    context = {'form': form}
    return render(request, 'gtech_produtos/new_tipo_produto.html', context)

def edit_tipo_produto(request, tipo_id):
    """Edita um tipo de produto existente."""
    tipo = TbTipoProduto.objects.get(cod=tipo_id)
    if request.method != 'POST':
        # Requisição inicial; preenche o formulário com a instância atual.
        form = TipoProdutoForm(instance=tipo)
    else:
        # Dados submetidos; processa os dados.
        form = TipoProdutoForm(instance=tipo, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tipo_produto'))
    context = {'tipo': tipo, 'form': form}
    return render(request, 'gtech_produtos/edit_tipo_produto.html', context)
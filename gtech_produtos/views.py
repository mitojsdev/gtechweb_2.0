from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from gtechwebs.models import TbTipoProduto, TbProduto
from .forms import TipoProdutoForm, ProdutoForm
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

def produto(request):
    """Página de produtos."""
    produtos = TbProduto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'gtech_produtos/produto.html', context)

def new_produto(request):
    """Adiciona um novo produto."""
    if request.method != 'POST':
        # Dados não submetidos; cria um formulário em branco.
        form = ProdutoForm()
    else:
        # Dados submetidos; processa os dados.
        form = ProdutoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto'))
    context = {'form': form}
    return render(request, 'gtech_produtos/new_produto.html', context)

def edit_produto(request, produto_id):
    """Edita um produto existente."""
    produto = TbProduto.objects.get(id_produto=produto_id)
    if request.method != 'POST':
        # Requisição inicial; preenche o formulário com a instância atual.
        form = ProdutoForm(instance=produto)
    else:
        # Dados submetidos; processa os dados.
        form = ProdutoForm(instance=produto, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto'))
    context = {'produto': produto, 'form': form}
    return render(request, 'gtech_produtos/edit_produto.html', context)
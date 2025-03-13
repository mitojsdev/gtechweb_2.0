from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from gtechwebs.models import TbTipoProduto, TbProduto
from gtechwebs.views import verifica_permissao
from .forms import TipoProdutoForm, ProdutoForm
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

@login_required
def tipo_produto(request):
    """Página de tipos de produtos."""
    tipos = TbTipoProduto.objects.all()
    context = {
        'tipos': tipos
    }
    return render(request, 'gtech_produtos/tipo_produto.html', context)

@login_required
@user_passes_test(verifica_permissao('gtechwebs', 'add_tbtipoproduto'),login_url='acesso_negado')
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

@login_required
@user_passes_test(verifica_permissao('gtechwebs','change_tbtipoproduto'),login_url='acesso_negado')
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

@login_required
def produto(request):
    """Página de produtos."""
    produtos = TbProduto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'gtech_produtos/produto.html', context)

@login_required
def search_produto(request):
    """Busca produtos pelo nome, fabricante, marca ou cor."""
    query = request.GET.get("q", "").strip()
    
    if query:
        produtos = TbProduto.objects.filter(
    Q(nome__icontains=query) | Q(fabricante__icontains=query) | Q(marca__icontains=query) | Q(cor__icontains=query)
    ).values("id_produto", "nome", "preco_custo", "tipo_produto__descricao", "fabricante", "marca", "cor", "id_fornecedor__nome_empresa", "data_cadastro", "estoque", "imagem")
        
        produtos_list = list(produtos)
        for produto in produtos_list:
            produto["data_cadastro"] = produto["data_cadastro"].strftime("%d/%m/%Y")  # Formata a data
            if produto["imagem"]:
                produto["imagem"] = settings.MEDIA_URL + str(produto["imagem"])
    else:
        produtos_list = []

    return JsonResponse({"produtos": produtos_list})

@login_required
@user_passes_test(verifica_permissao('gtechwebs','add_tbproduto'), login_url='acesso_negado')
def new_produto(request):
    """Adiciona um novo produto."""
    if request.method != 'POST':
        # Dados não submetidos; cria um formulário em branco.
        form = ProdutoForm()
    else:
        # Dados submetidos; processa os dados.
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto'))
    context = {'form': form}
    return render(request, 'gtech_produtos/new_produto.html', context)

@login_required
@user_passes_test(verifica_permissao('gtechwebs','change_tbproduto'), login_url='acesso_negado')
def edit_produto(request, produto_id):
    """Edita um produto existente."""
    produto = TbProduto.objects.get(id_produto=produto_id)
    if request.method != 'POST':
        # Requisição inicial; preenche o formulário com a instância atual.
        form = ProdutoForm(instance=produto)
    else:
        # Dados submetidos; processa os dados.
        form = ProdutoForm(instance=produto, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto'))
    context = {'produto': produto, 'form': form}
    return render(request, 'gtech_produtos/edit_produto.html', context)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from gtechwebs.models import TbVenda, TbProduto
from .forms import VendaForm
from django.db.models import Q
from datetime import datetime


# Create your views here.
#def venda(request):
 #   """View para a página de vendas realizadas."""
 #   vendas = TbVenda.objects.all()
  #  context = {
  #      'vendas': vendas
  #  }
  #  return render(request, 'gtech_vendas/venda.html', context)


def venda(request):
    query = request.GET.get("q", "").strip()
    data_inicio = request.GET.get("data_inicio", "")
    data_fim = request.GET.get("data_fim", "")
    
    vendas = TbVenda.objects.all()

    # Filtro por nome do cliente ou nome do produto
    if query:
        vendas = vendas.filter(
            Q(id_cliente__nome__icontains=query) |  
            Q(id_produto__nome__icontains=query) |
            Q(id_produto__id_fornecedor__nome_empresa__icontains=query)
        )

    # Filtro por intervalo de datas
    if data_inicio:
        vendas = vendas.filter(data__gte=datetime.strptime(data_inicio, "%Y-%m-%d"))
    if data_fim:
        vendas = vendas.filter(data__lte=datetime.strptime(data_fim, "%Y-%m-%d"))

    context = {"vendas": vendas}

    return render(request, 'gtech_vendas/venda.html', context)


def new_venda(request):
    """Adiciona uma nova venda."""
    if request.method != 'POST':
        # Dados não submetidos; cria um formulário em branco.
        form = VendaForm()
    else:
        # Dados submetidos; processa os dados.
        form = VendaForm(data=request.POST)
        if form.is_valid():
            venda = form.save(commit=False)

            # Calcula o lucro
            produto = get_object_or_404(TbProduto, id_produto=venda.id_produto.id_produto)
            lucro = (venda.preco_venda - produto.preco_custo) * venda.quantidade
            venda.lucro = lucro
            venda.save()

            return HttpResponseRedirect(reverse('venda'))
    context = {'form': form}
    return render(request, 'gtech_vendas/new_venda.html', context)

def edit_venda(request, venda_id):
    """Edita uma venda."""
    venda = get_object_or_404(TbVenda, id=venda_id)
    if request.method != 'POST':
        # Requisição inicial; preenche o formulário com a instância atual.
        form = VendaForm(instance=venda)
    else:
        # Dados de POST submetidos; processa os dados.
        form = VendaForm(instance=venda, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('venda'))
    context = {'venda': venda, 'form': form}
    return render(request, 'gtech_vendas/edit_venda.html', context)

def get_preco_custo(request, produto_id):
    """Retorna o preço de custo de um produto."""
    try:
        produto = TbProduto.objects.get(pk=produto_id)
        data = {'preco_custo': produto.preco_custo, 'margem': produto.tipo_produto.margem}
    except TbProduto.DoesNotExist:
        data = {'preco_custo': None}
    return JsonResponse(data) 
    
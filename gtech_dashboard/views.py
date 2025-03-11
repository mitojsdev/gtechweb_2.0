from django.shortcuts import render
from django.db.models import Count, Sum
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.offline as opy
from gtechwebs.models import TbVenda, TbFornecedor, TbCliente, TbProduto
import pandas as pd
from django.db import models
from django.utils import timezone
from django.db.models import Count
import plotly.express as px
import plotly.io as pio

# Create your views here.
def dashboard(request):
    #contagem geral do projeto
    total_clientes = TbCliente.objects.count()
    total_fornecedores = TbFornecedor.objects.count()
    total_produtos = TbProduto.objects.count()    

    #vendas dos últimos 10 dias
    data_inicio = datetime.today() - timedelta(days=10)
    vendas = TbVenda.objects.filter(data__gte=data_inicio)

    #total de vendas
    total_vendas = vendas.aggregate(Sum('preco_venda'))['preco_venda__sum'] or 0

    total_lucro = vendas.aggregate(Sum('lucro'))['lucro__sum'] or 0

    #agrupando vendas por produto    
    vendas_por_produto = vendas.values('id_produto__nome').annotate(total=Count('id_produto'))


    #criando gráfico de barras
    produtos = [venda['id_produto__nome'] for venda in vendas_por_produto]
    quantidades = [venda['total'] for venda in vendas_por_produto]

    fig = go.Figure(data=[go.Bar(x=produtos,y=quantidades)])
    fig.update_layout(title='Vendas por Produto (últimos 10 dias)', xaxis_title='Produto',yaxis_title='Quantidade')

    grafico = opy.plot(fig,output_type='div')

    contexto = {
        'total_clientes': total_clientes,
        'total_fornecedores': total_fornecedores,
        'total_produtos': total_produtos,
        'total_vendas': total_vendas,
        'total_lucro': total_lucro,
        'grafico': grafico,
    }

    return render(request,'gtech_dashboard/inicio.html', contexto)
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from gtechwebs.models import TbVenda
#from .forms import TipoProdutoForm, ProdutoForm

# Create your views here.
def venda(request):
    """View para a página de vendas realizadas."""
    vendas = TbVenda.objects.all()
    context = {
        'vendas': vendas
    }
    return render(request, 'gtech_vendas/venda.html', context)

    
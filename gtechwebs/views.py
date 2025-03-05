from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from . forms import ClienteForm, FornecedorForm
from . models import TbCliente, TbFornecedor


# Create your views here.
def index(request):
    """Página incial do site."""
    return render(request, 'gtechwebs/index.html')

def clientes(request):
    """Página de clientes."""
    cli = TbCliente.objects.all()
    context = {
        'clientes': cli
    }
    return render(request, 'gtechwebs/clientes.html', context)

def new_cliente(request):
    """Página de cadastro de clientes."""
    if request.method != 'POST':
        form = ClienteForm()
    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('clientes'))
    context = {'form': form}
    return render(request, 'gtechwebs/new_cliente.html', context)

def edit_cliente(request, id_cliente):
    """Página de edição de clientes."""
    cli = TbCliente.objects.get(id_cliente=id_cliente)
    if request.method != 'POST':
        form = ClienteForm(instance=cli)
    else:
        form = ClienteForm(instance=cli, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('clientes'))
    context = {'cliente': cli, 'form': form}
    return render(request, 'gtechwebs/edit_cliente.html', context)

def fornecedores(request):
    """Página de fornecedores."""
    fornecedores = TbFornecedor.objects.all()
    context = {
        'fornecedores': fornecedores
    }
    return render(request, 'gtechwebs/fornecedores.html', context)

def new_fornecedor(request):
    """Página de cadastro de fornecedores."""
    if request.method != 'POST':
        form = FornecedorForm()
    else:
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fornecedores'))
    context = {'form': form}
    return render(request, 'gtechwebs/new_fornecedor.html', context)

def edit_fornecedor(request, id_fornecedor):
    """Página de edição de fornecedores."""
    fornecedor = TbFornecedor.objects.get(id_fornecedor=id_fornecedor)
    if request.method != 'POST':
        form = FornecedorForm(instance=fornecedor)
    else:
        form = FornecedorForm(instance=fornecedor, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fornecedores'))
    context = {'fornecedor': fornecedor, 'form': form}
    return render(request, 'gtechwebs/edit_fornecedor.html', context)
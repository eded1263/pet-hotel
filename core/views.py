from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from core.forms import FormCliente, FormPet
from core.models import Cliente, Pet, Plano


# Create your views here.

def home(request):
    return render(request, 'core/index.html')


@login_required
def reserva(request):
    return render(request, 'core/tabela.html')


def planos(request):
    contexto = {'planos': Plano.objects.all()}
    return render(request, 'core/planos.html', contexto)


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


@login_required
def cadastro_cliente(request):
    if request.user.is_staff:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        else:
            contexto = {'form': form, 'texto_titulo': 'Cadastro de Cliente',
                        'texto_botao': 'Cadastrar', 'url_voltar': 'url_principal'}
            return render(request, 'core/cadastro_clientes.html', contexto)
    else:
        return render(request, 'core/nao_autorizado.html')


@login_required
def listagem_clientes(request):
    if request.user.is_staff:
        dados = Cliente.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_clientes.html', contexto)
    else:
        return render(request, 'core/nao_autorizado.html')


@login_required
def cadastro_pets(request):
    form = FormPet(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form, 'texto_titulo': 'Cadastro de Cliente', 'texto_botao': 'Cadastrar',
                'url_voltar': 'url_principal'}
    return render(request, 'core/cadastro_pets.html', contexto)


@login_required
def listagem_pets(request):
    dados = Pet.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_pets.html', contexto)


def tabela(request):
    return render(request, 'core/tabela.html')


@login_required
def atualiza_cliente(request):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=request.user.id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('listagem_clientes')
        else:
            contexto = {'form': form, 'texto_titulo': 'Atualização de Cliente',
                        'texto_botao': 'Atualizar', 'url_voltar': 'listagem_clientes'}
            return render(request, 'core/cadastro_clientes.html', contexto)
    else:
        return render(request, 'core/nao_autorizado.html')


def exclui_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        if request.POST:
            obj.delete()
            return redirect('listagem_clientes')
        else:
            contexto = {'dados': obj.nome, 'id': obj.id, 'url': 'listagem_clientes'}
            return render(request, 'core/confirma_exclusao.html', contexto)
    else:
        return render(request, 'core/nao_autorizado.html')

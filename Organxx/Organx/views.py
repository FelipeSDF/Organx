from django.shortcuts import render,redirect
from .models import Cadastrados
from .forms import CadForm, UpdateForm

from django.contrib import messages
from django.http import cookie

def adicionar(request):
    if CadForm(request.POST).is_valid():
        form = CadForm(request.POST)
        form.save()
        # messages.success(request, 'Adicionado com Sucesso')
        messages.success(request, "Adicionado com sucesso")
        return redirect(add_page)
    else:
        messages.error(request, "Houve um erro")
        return redirect(add_page)

def add_page(request):
    if request.method == 'GET':
        form = CadForm(request.GET)
        
    return render(request, 'add.html', {'form':form})

def consulta_page(request):
    pessoas = Cadastrados.objects.all()
    pessoas = pessoas.order_by('nome')

    return render(request, 'consultar.html', {'pessoas':pessoas})

def page(request, page):
    
    if page == 'home':
        return redirect(to=home)
    
    if page == 'consultar':
        pessoas = Cadastrados.objects.all()
        pessoas = pessoas.order_by('nome')

        return render(request, 'consultar.html', {'pessoas':pessoas})
    if page == 'editar':
        return render(request, 'editar.html', {})
    
    if page == 'filtrar':
        pessoas = Cadastrados.objects.all()
        return render(request, 'filtros.html', {'filtros':True, 'pessoas': pessoas})

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})
        
def consulta(request):
    
    if request.method == 'GET':
        nome_query = request.GET.get('query')
        pessoa = Cadastrados.objects.filter(nome__contains = nome_query)
        
        if len(pessoa) > 1:
            try:
                pessoa = Cadastrados.objects.get(nome = nome_query)
                
                return render(request, 'consultar.html', {'query':pessoa})
            except:
                return render(request, 'consultar.html', {'pessoas':pessoa})
                
        elif len(pessoa) == 1: 
            pessoa = Cadastrados.objects.get(nome = pessoa[0].nome)
            return render(request, 'consultar.html', {'query':pessoa})
        else: 
            print('c')
            return render(request, 'consultar.html', {'query':pessoa})
        
    elif request.method == 'POST':
        nome_query = request.POST.get('nome_query')
        acao = request.POST.get('acao')
        
        if acao == 'editar':
            editar = Cadastrados.objects.get(nome = nome_query)
            form = UpdateForm(instance=editar)
            
            return render(request, 'consultar.html', {'query':editar,'editar':'editar', 'deletar':'False', 'form': form})
        
        elif acao == 'deletar':
            nome_antigo = request.POST.get('nome_query')
            deletar = Cadastrados.objects.get(nome = nome_antigo)
            deletar.delete()

            pessoas = Cadastrados.objects.all()
            pessoas = pessoas.order_by('nome')

        return render(request, 'consultar.html', {'pessoas':pessoas,'deletar':'deletar','editar':'False'})
        
def editar(request):
    nome_antigo = request.POST.get('nome_query')
    pessoa = Cadastrados.objects.get(nome = nome_antigo)
    
    form = UpdateForm(request.POST, instance=pessoa)
    
    if form.is_valid():
        form.save()
    
    messages.success(request, 'Dados editados com sucesso')
    return redirect(to=consulta_page)
    # return render(request, 'consultar.html', {'query':pessoa})

def filtrar(request):
    empresa = request.GET.get('empresa')
    unidade = request.GET.get('unidade')
    
    if empresa != '' and unidade != '':
        pessoa = Cadastrados.objects.filter(empresa__contains = empresa, unidade__contains = unidade)
        return render(request, 'filtros.html', {'filtros':True, 'pessoas': pessoa})
    
    elif empresa != '' and unidade == '':
        empresa = Cadastrados.objects.filter(empresa__contains = empresa)
        return render(request, 'filtros.html', {'filtros':True, 'pessoas': empresa})
        
    elif empresa == '' and unidade != '':
        unidade = Cadastrados.objects.filter(unidade__contains = unidade)
        return render(request, 'filtros.html', {'filtros':True, 'pessoas': unidade})
    
    else:
        pessoas = Cadastrados.objects.all()
        return render(request, 'filtros.html', {'filtros':True, 'pessoas': pessoas})
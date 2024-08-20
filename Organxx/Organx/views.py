from django.shortcuts import render
from .models import Cadastrados
from django.contrib import messages 

def adicionar(email,nome,telefone,cargo,empresa,unidade,Função):

    pessoas = Cadastrados(nome=nome,telefone=telefone,empresa=empresa,unidade=unidade)
    pessoas.save()

def page(request, page):
    
    if page == 'home':
        return render(request, 'home.html', {})
    if page == 'cadastrar':

        if request.method == 'POST':
            email = request.POST.get('email')
            nome = request.POST.get('nome')
            telefone = request.POST.get('telefone')
            cargo = request.POST.get('cargo_radio')
            empresa = request.POST.get('Empresa')
            unidade = request.POST.get('Unidade')
            funcao = request.POST.get('funcao')

            if nome != '' and email != '' and telefone != '' and cargo != '' and empresa != '' and unidade != '' and funcao != '':
                adicionar(email,nome,telefone,cargo,empresa,unidade,funcao)
                print('adicionado!')
            else:
                print('preencha todos os dados')
            return render(request, 'add.html', {})
        
        return render(request, 'add.html', {})
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
            
            return render(request, 'consultar.html', {'query':editar,'editar':'editar', 'deletar':'False'})
        
        elif acao == 'deletar':
            nome_antigo = request.POST.get('nome_query')
            deletar = Cadastrados.objects.get(nome = nome_antigo)
            deletar.delete()
            print(deletar)

            pessoas = Cadastrados.objects.all()
            pessoas = pessoas.order_by('nome')

        return render(request, 'consultar.html', {'pessoas':pessoas,'deletar':'deletar','editar':'False'})
        
def editar(request):
    
    nome = request.POST.get('nome')
    nome_antigo = request.POST.get('nome_query')
    empresa = request.POST.get('Empresa')
    unidade = request.POST.get('unidade')
    telefone = request.POST.get('telefone')

    Cadastrados.objects.filter(nome = nome_antigo).update(nome =f'{nome}', empresa = f'{empresa}', unidade =f'{unidade}', telefone =f'{telefone}')
    pessoa = Cadastrados.objects.get(nome = nome)

    return render(request, 'consultar.html', {'query':pessoa})

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
from django.shortcuts import render
from .models import Cadastrados

def adicionar(email,nome,telefone,cargo,empresa,unidade,Função):

    pessoas = Cadastrados(email=email,nome=nome,telefone=telefone,cargo=cargo,empresa=empresa,unidade=unidade,Função=Função)
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

            print(unidade)

            if nome != '' and email != '' and telefone != '' and cargo != '' and empresa != '' and unidade != '' and funcao != '':
                adicionar(email,nome,telefone,cargo,empresa,unidade,funcao)
                print('adicionado!')
            else:
                print('preencha todos os dados')
            return render(request, 'add.html', {'added':nome[0:5]})
        
        return render(request, 'add.html', {})
    if page == 'consultar':
        pessoas = Cadastrados.objects.all()
        pessoas = pessoas.order_by('data_add').reverse()
        pessoas = pessoas[:10]

        return render(request, 'consultar.html', {'pessoas':pessoas})
    if page == 'editar':
        return render(request, 'editar.html', {})
  
def home(request):
    return render(request, 'home.html', {})

def consulta(request):
    try:
        nome_query = request.GET.get('query')
        pessoa = Cadastrados.objects.get(nome = nome_query)
        print(pessoa)
        return render(request, 'consultar.html', {'query':pessoa})
    except:
        print('deu m')
        return render(request, 'consultar.html', {})
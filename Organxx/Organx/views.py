from django.shortcuts import render

def page(request, page):
    
    if page == 'home':
        return render(request, 'home.html', {})
    if page == 'cadastrar':
        return render(request, 'add.html', {})
    if page == 'consultar':
        return render(request, 'consultar.html', {})
    if page == 'alterar':
        return render(request, 'alterar.html', {})
    if page == 'login':
        return render(request, 'login.html', {})

def home(request):
    return render(request, 'home.html', {})

def land_page(request):
    return render(request, 'land.html', {})
def add_page(request):
    return render(request, 'add.html', {}) 
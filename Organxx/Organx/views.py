from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def land_page(request):
    return render(request, 'land.html', {})
def add_page(request):
    return render(request, 'add.html', {}) 
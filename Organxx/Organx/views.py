from django.shortcuts import render

def land_page(request):
    render(request, 'land.html', {})

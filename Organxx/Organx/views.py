from django.shortcuts import render

def land_page(request):
    return render(request, 'land.html', {})

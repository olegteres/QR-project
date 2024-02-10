from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories 

def index(request):
    
    categories = Categories.objects.all()
    
    
    context = {
        'title': 'QR - Главная',
        'content': 'QR-проект',
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'QR - О нас',
        'content': 'О нас',
        'text_on_page': 'Демонстрационный текст'
    }
    return render(request, 'main/about.html', context)
from django.shortcuts import render

# Create your views here.

def index_favoritos(request):
    return render(request, 'index.html')

def crear(request):
    return render(request, 'crear.html')

def lista(request):
    return render(request, 'lista.html')
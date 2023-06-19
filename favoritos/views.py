from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Favorito
from .forms import FavoritoModelForm

# Create your views here.

def index_favoritos(request):
    return render(request, 'index.html')

def crear(request):

    form = FavoritoModelForm()
    if request.method == 'POST':
        form = FavoritoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('favoritos:lista'))
        else:
            print(form.errors)   
    context = {'form' : form} 
    return render(request, 'crear.html', context)

def lista(request):

    objetos = Favorito.objects.all()
    contexto = {
        'favoritos' : objetos,
    }
    
    return render(request, 'lista.html', contexto)

def borrar(request):
    pass
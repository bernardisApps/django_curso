from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Favorito
from .forms import FavoritoModelForm

def crear(request):

    titulo = 'Crear'

    form = FavoritoModelForm()
    if request.method == 'POST':
        form = FavoritoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('favoritos:lista'))
        else:
            print(form.errors)   
    context = {
        'form' : form,
        'titulo' : titulo
        } 
    return render(request, 'crear.html', context)

def lista(request):

    objetos = Favorito.objects.all()
    contexto = {
        'favoritos' : objetos,
    }
    
    return render(request, 'lista.html', contexto)

def borrar(request, pk):
    Favorito.objects.get(pk=pk).delete()
    return redirect(reverse('favoritos:lista'))

def editar(request, pk):

    titulo = 'Editar'

    obj = Favorito.objects.get(pk=pk)

    if request.method == 'POST':
        form = FavoritoModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('favoritos:lista'))
    else:
        form = FavoritoModelForm(instance = obj)
    context = {
        'form' : form,
        'titulo' : titulo
    }
    return render(request,'crear.html', context)
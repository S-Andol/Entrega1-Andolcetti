from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import SuperHeroe
from django.shortcuts import render, redirect
from inicio.forms import CreacionSuperHereoFormulario,BuscarSuperHeroe
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView  


def mi_vista(request):
    return render(request,'inicio/index.html')

# Create your views here.
"""
def crear_superheroe(request):
    if request.method == "POST":
        formulario = CreacionSuperHereoFormulario(request.POST)
        
        if formulario.is_valid():
        # limita al usuario a colocar cosas que estan malas como en la edad
            datos_correctos = formulario.cleaned_data

            superheroe = SuperHeroe (nombre = request.POST['nombre'], superpoder = request.POST['superpoder'], motivo = request.POST['motivo'], autor = request.POST['autor'])
            superheroe.save()
            

            return redirect('inicio:listar_superheroes')
            
    formulario = CreacionSuperHereoFormulario()
    return render(request, 'inicio/crear_superheroe.html',{'formulario': formulario})
"""

# def lista_superheroes(request):
#     return render(request, 'inicio/lista_superheroes.html')

    
# def lista_superheroes(request):
#     nombre_a_buscar = request.GET.get('nombre',None)
    
#     if nombre_a_buscar:
#         SuperHeroes = SuperHeroe.objects.filter(nombre__icontains = nombre_a_buscar)
#     else:
#         SuperHeroes = SuperHeroe.objects.all()
#     formulario_busqueda = BuscarSuperHeroe()
#     return render(request, 'inicio/lista_superheroes.html',{'superheroes':SuperHeroes,'formulario':formulario_busqueda})


def sobre_mi(request):
    return render(request,'inicio/sobre_mi.html')

class SuperHeroeListView(ListView):
    model = SuperHeroe
    template_name = "inicio/lista_superheroes.html"
    
class SuperHeroeDetailView(DetailView):
    model = SuperHeroe
    template_name = "inicio/detalle_superheroe.html"

class SuperHeroeCreateView(CreateView):
    model = SuperHeroe
    template_name = "inicio/crear_superheroe.html"
    fields = ['nombre','superpoder','motivo','autor']
    success_url = '/inicio/superheroes/'

class SuperHeroeUpdateView(UpdateView):
    model = SuperHeroe
    template_name = "inicio/modificar_superheroe.html"
    fields = ['nombre','superpoder','motivo','autor']
    success_url = '/inicio/superheroes/'


class SuperHeroeDeleteView(DeleteView):
    model = SuperHeroe
    template_name = "inicio/eliminar_superheroe.html"
    success_url = '/inicio/superheroes/'




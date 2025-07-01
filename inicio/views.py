from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from inicio.models import Articulo
import random
from inicio.forms import CrearForm, BusquedaForm, EditarForm
from django.contrib.auth.decorators import login_required


    
def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_articulo(request):
 
    formulario = CrearForm()
    
    if request.method == 'POST':
        formulario = CrearForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            articulo = Articulo(
                articulo=data.get('Artículo'),
                descripcion=data.get('Descripción'),
                precio=data.get('Precio')
            )
            articulo.save()
            
            return redirect('inicio:listado_articulo')
    return render(request, 'inicio/crear_articulo.html', {'formulario': formulario})


def listado_articulo(request):

    formulario_busqueda = BusquedaForm(request.GET)
    if formulario_busqueda.is_valid():
        articulo_buscado = formulario_busqueda.cleaned_data.get('Artículo')
        descripcion_buscada = formulario_busqueda.cleaned_data.get('Descripción')
        lista_articulo = Articulo.objects.filter(articulo__icontains=articulo_buscado, descripcion__icontains=descripcion_buscada)
    else:
        lista_articulo = []
    
    formulario_busqueda = BusquedaForm()
    return render(request, 'inicio/listado_articulo.html', {'listado_articulo': lista_articulo, 'formulario_busqueda': formulario_busqueda})

def ver_articulo(request, id_articulo):
    articulo = Articulo.objects.get(id=id_articulo)
    return render(request, 'inicio/ver_articulo.html', {'articulo': articulo})

@login_required
def eliminar_articulo(request, id_articulo):
    articulo = Articulo.objects.get(id=id_articulo)
    articulo.delete()
    return render(request, 'inicio/eliminar_articulo.html', {'articulo': articulo})

@login_required
def editar_articulo(request, id_articulo):
    articulo = Articulo.objects.get(id=id_articulo)
    formulario = EditarForm(initial={'Artículo': articulo.articulo, 'Descripción': articulo.descripcion, 'Precio': articulo.precio})
    
    if request.method == 'POST':
        formulario = EditarForm(request.POST)
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            articulo.articulo = data.get('Artículo')
            articulo.descripcion = data.get('Descripción')
            articulo.precio = data.get('Precio')
            articulo.save()
            
            return redirect('inicio:listado_articulo')
    return render(request, 'inicio/editar_articulo.html', {'formulario': formulario, 'articulo': articulo})
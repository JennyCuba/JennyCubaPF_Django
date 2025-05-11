from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
from inicio.models import Articulo
import random
from inicio.forms import RegistroArticuloForm, BusquedaForm
from django.shortcuts import redirect

    
def inicio(request):
    return render(request, 'inicio/inicio.html')
    #return HttpResponse ('<h1>Bienvenida!<h1/>')

def crear_articulo(request):
 
    formulario = RegistroArticuloForm()
    
    if request.method == 'POST':
        formulario = RegistroArticuloForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            articulo = Articulo(
                articulo=data.get('articulo'),
                descripcion=data.get('descripcion'),
                precio=data.get('precio')
            )
            articulo.save()
            
            return redirect('inicio:crear_articulo')
    return render(request, 'inicio/crear_articulo.html', {'formulario': formulario})


def listado_articulo(request):

    formulario_busqueda = BusquedaForm(request.GET)
    if formulario_busqueda.is_valid():
        articulo_buscado = formulario_busqueda.cleaned_data.get('articulo')
        descripcion_buscada = formulario_busqueda.cleaned_data.get('descripcion')
        lista_articulo = Articulo.objects.filter(articulo__icontains=articulo_buscado, descripcion__icontains=descripcion_buscada)
    else:
        lista_articulo = []
    
    formulario_busqueda = BusquedaForm()
    return render(request, 'inicio/listado_articulo.html', {'listado_articulo': lista_articulo, 'formulario_busqueda': formulario_busqueda})

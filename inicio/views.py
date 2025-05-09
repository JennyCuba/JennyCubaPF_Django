from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
from inicio.models import Articulo, Registro
import random
from inicio.forms import RegistroArticuloForm, RegistroForm
from django.shortcuts import redirect

def bienvenida(request):
    return render(request, 'inicio/bienvenida.html')
    #return HttpResponse ('<h1>Bienvenida!<h1/>')
    
def inicio(request):
    return render(request, 'inicio/inicio.html')
    #return HttpResponse ('<h1>Bienvenida!<h1/>')

def fecha_y_hora(request):
    fecha_y_hora = datetime.now()
    return HttpResponse (f'<h1>esta vista muestra la fecha y hora<h1/>\n{fecha_y_hora}')

def saludo(request, nombre, apellido):
    nombre_formateado = nombre.title()
    apellido_formateado = apellido.title()
    return HttpResponse(f"Buenas {nombre_formateado} {apellido_formateado}, como va?")

def mi_template(request):
    
# V1
    #archivo_abierto = open('Templates\mi_template.html')
    #template = Template(archivo_abierto.read())
    #archivo_abierto.close()
    
    #contexto = Context({'Nombre': 'Jenny'})
    #template_renderizado = template.render(contexto)

    #return HttpResponse(template_renderizado)
    
# v2 con cargador y shortcuts
    template = loader.get_template('inicio/mi_template.html')
    return render(request, 'inicio/mi_template.html', {'Nombre': 'Jenny'})


def mi_template2(request):
    
# v1 ejemplo template con cargador
    #template = loader.get_template('mi_template2.html')
    #diccionario = {'Nombre': 'Jenny'}
    #template_renderizado = template.render(diccionario)

    #return HttpResponse(template_renderizado)
# v2 resumida
    template = loader.get_template('inicio/mi_template2.html')
    return render(request, 'inicio/mi_template2.html')

def condicionales_y_bucles(request):
    
   
    return render(request, 'inicio/condicionales_y_bucles.html',  {
        'Nombre': 'Jenny',
        'Mis_elementos': [22],
        'Numeros': list(range(15))
    })
    
#def crear_articulo(request, articulo, descripcion, precio):
    # articulo = Articulo(articulo= articulo, descripcion= descripcion, precio=precio)
    # articulo.save()
    # return render(request, 'inicio/crear_articulo.html', {'articulo':articulo})

def crear_articulo(request):
    print('*************************************************************************************')
    print('request', request)
    print('GET', request.GET)
    print('POST', request.POST)
    print('*************************************************************************************')
    
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

def registro_articulo(request):
    print('*************************************************************************************')
    print('request', request)
    print('GET', request.GET)
    print('POST', request.POST)
    print('*************************************************************************************')
    
    formulario1 = RegistroForm()
    
    if request.method == 'POST':
        formulario1 = RegistroForm(request.POST)
        if formulario1.is_valid():
            data = formulario1.cleaned_data
        
            articulo = Registro(
                articulo=data.get('articulo'),
                descripcion=data.get('descripcion'),
                precio=data.get('precio')
            )
            articulo.save()
            
            return redirect('inicio:registro_articulo')
    return render(request, 'inicio/registro_articulo.html', {'formulario': formulario1})

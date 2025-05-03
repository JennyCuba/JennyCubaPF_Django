from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
from inicio.models import Articulo
import random

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
    
def crear_articulo(request, articulo, descripcion, precio):
    #auto = Auto(marca=random.choice(['Ford', 'Fiat', 'Chevrolet', 'Ferrari', 'Mercedes']), modelo='Generico', anio=random.choice([2020, 2021, 2022, 2023, 2024]))
    articulo = Articulo(articulo= articulo, descripcion= descripcion, precio=precio)
    articulo.save()
    return render(request, 'inicio/registro_articulo.html', {'articulo':articulo})

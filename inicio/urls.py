from inicio.views import bienvenida, fecha_y_hora, mi_template, saludo, mi_template2, condicionales_y_bucles, crear_articulo, inicio
from django.urls import path

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('bienvenida/', bienvenida, name='bienvenida'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('fecha_y_hora/', fecha_y_hora, name='fecha_y_hora'),
    path('mi_template/', mi_template, name='mi_template'),
    path('mi_template2/', mi_template2, name='mi_template2'),
    path('condicionales_y_bucles/', condicionales_y_bucles, name='condicionales_y_bucles'),
    path('crear_articulo/<str:marca>/<str:modelo>/<int:anio>/', crear_articulo, name='crear_articulo'),
]
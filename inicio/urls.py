# from inicio.views import bienvenida, fecha_y_hora, mi_template, saludo, mi_template2, condicionales_y_bucles, crear_articulo, inicio, registro_articulo
from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('listado_articulos/', views.listado_articulo, name='listado_articulo'),
]
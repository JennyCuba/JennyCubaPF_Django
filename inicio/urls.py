from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('articulo/registro', views.crear_articulo, name='crear_articulo'),
    path('articulo/', views.listado_articulo, name='listado_articulo'),
    path('articulo/<int:id_articulo>/', views.ver_articulo, name='ver_articulo'),
    path('articulo/<int:id_articulo>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),
    path('articulo/<int:id_articulo>/editar/', views.editar_articulo, name='editar_articulo'),
]
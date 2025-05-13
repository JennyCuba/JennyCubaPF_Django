from django.urls import path
from stock import views

app_name = 'stock'

urlpatterns = [

    path('', views.ListadoMovimientos.as_view(), name='listado_movimientos'),
    path('movimientos/', views.RegistrarMovimientos.as_view(), name='registrar_movimientos'),
   
]

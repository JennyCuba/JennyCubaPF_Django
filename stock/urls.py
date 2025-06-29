from django.urls import path
from stock import views

app_name = 'stock'

urlpatterns = [

    path('movimientos', views.ListadoMovimientos.as_view(), name='listado_movimientos'),
    path('movimientos/registrar', views.RegistrarMovimientos.as_view(), name='registrar_movimientos'),
    path('movimientos/<int:pk>/', views.DetalleMovimientos.as_view(), name='detalle_movimientos')
   
]

from django.urls import path
from stock import views

app_name = 'stock'

urlpatterns = [

    path('stock/', views.listado_stock.as_view(), name='listado_stock'),
   
]

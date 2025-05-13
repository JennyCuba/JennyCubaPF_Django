from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from stock.models import MovimientoStock

# Create your views here.
class ListadoMovimientos(ListView):
    model = MovimientoStock
    template_name = 'stock/listado_movimientos.html'
    context_object_name = 'movimientos'
    ordering = ['-fecha']
    
class RegistrarMovimientos(CreateView):
    model = MovimientoStock
    fields = ['articulo', 'tipo', 'cantidad', 'observaciones']
    template_name = 'stock/registrar_movimientos.html'
    success_url = reverse_lazy('stock:listado_movimientos')
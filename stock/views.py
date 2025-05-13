from django.shortcuts import render
from django.views.generic.list import ListView
from stock.models import MovimientoStock

# Create your views here.
class listado_stock(ListView):
    model = MovimientoStock
    template_name = 'stock/listado_stock.html'
    context_object_name = 'movimientos'
    ordering = ['-fecha']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Movimientos de Stock'
        return context
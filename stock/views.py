from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from stock.models import MovimientoStock
from django.contrib.auth.mixins import LoginRequiredMixin
from stock.forms import ActualizarStockForm


# Create your views here.
class ListadoMovimientos(ListView):
    model = MovimientoStock
    template_name = "stock/listado_movimientos.html"
    context_object_name = 'listado_movimientos'
    ordering = ['-fecha']
    
class RegistrarMovimientos(CreateView):
    model = MovimientoStock
    fields = ['articulo', 'tipo', 'cantidad', 'observaciones']
    template_name = "stock/registrar_movimientos.html"
    success_url = reverse_lazy('stock:listado_movimientos')
    
class DetalleMovimientos(DetailView):
    model = MovimientoStock
    template_name = "stock/detalle_movimientos.html"
        
class EditarMovimientos(UpdateView):
    model = MovimientoStock
    fields = ['articulo', 'tipo', 'cantidad', 'observaciones']
    template_name = "stock/editar_movimientos.html"
    #form_class = ActualizarStockForm
    success_url = reverse_lazy('stock:listado_movimientos')

class EliminarMovimientos(DeleteView):
    model = MovimientoStock
    template_name = "stock/eliminar_movimientos.html"
    success_url = reverse_lazy('stock:listado_movimientos')  

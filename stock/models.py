from django.db import models

class MovimientoStock(models.Model):
    articulo = models.ForeignKey('inicio.Articulo', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('salida', 'Salida')])
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)
    
    def __str__(self):
        return f"Artículo: {self.articulo}, Tipo: {self.tipo}, Cantidad: {self.cantidad}, Fecha: {self.fecha}, Observaciones: {self.observaciones}"

# Create your models here.

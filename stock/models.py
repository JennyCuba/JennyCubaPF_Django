from django.db import models

class MovimientoStock(models.Model):
    articulo = models.ForeignKey('inicio.Articulo', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('salida', 'Salida')])
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)
    
    def __str__(self):
        return f"Movimiento: {self.id}, Tipo: {self.tipo}, Cantidad: {self.cantidad}, Fecha: {self.fecha}, Observaciones: {self.observaciones}"


#class Stock(models.Model):
    #articulo = models.ForeignKey('inicio.Articulo', on_delete=models.CASCADE)
    #cantidad = models.PositiveIntegerField(default=0)
    
    #def __str__(self):
        #return f"Stock de {self.articulo.nombre}: {self.cantidad} unidades"
    
    #def actualizar_stock(self, cantidad, tipo):
        #if tipo == 'entrada':
            #self.cantidad += cantidad
        #elif tipo == 'salida':
            #self.cantidad -= cantidad
        #self.save() 
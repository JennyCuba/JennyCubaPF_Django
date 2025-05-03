from django.db import models

class Articulo(models.Model):
    articulo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    precio = models.IntegerField()
    
    def __str__(self):
        return f"Auto({self.id}): {self.articulo} - {self.descripcion}"

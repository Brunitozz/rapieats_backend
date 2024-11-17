from django.db import models
from .producto import Producto
from .combo import Combo
from .producto import Ingrediente

class Personalizacion(models.Model):
    id_personalizacion = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    precio_adicional = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.precio_adicional}"


class DetalleAdicional(models.Model):
    id_detalle_adicional = models.AutoField(primary_key=True)
    producto_ingrediente = models.ForeignKey(
        Ingrediente, on_delete=models.CASCADE
    )
    personalizacion = models.ForeignKey(Personalizacion, on_delete=models.CASCADE)
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
    precio_adicional_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"DetalleAdicional {self.id_detalle_adicional}"

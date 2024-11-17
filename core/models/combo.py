from django.db import models
from .producto import Producto

class Combo(models.Model):
    id_combo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class ComboProducto(models.Model):
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        unique_together = ('combo', 'producto')

    def __str__(self):
        return f"{self.combo} - {self.producto}"

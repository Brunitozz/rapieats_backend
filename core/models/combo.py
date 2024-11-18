from django.db import models
from .producto import Producto

class Combo(models.Model):
    id_combo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'combo'


class ComboProducto(models.Model):
    id_combo = models.ForeignKey(Combo, on_delete=models.CASCADE, db_column='id_combo')
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'combo_producto'
        unique_together = (('id_combo', 'id_producto'),)

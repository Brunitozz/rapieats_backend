from django.db import models
from .producto import Producto
from .combo import Combo
from .producto_ingrediente import ProductoIngrediente


class Personalizacion(models.Model):
    id_personalizacion = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')
    tipo = models.CharField(max_length=50)
    precio_adicional = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personalizacion'


class DetalleAdicional(models.Model):
    id_detalle_adicional = models.AutoField(primary_key=True)
    id_producto_ingrediente = models.ForeignKey(ProductoIngrediente, on_delete=models.CASCADE, db_column='id_producto_ingrediente')
    id_personalizacion = models.ForeignKey(Personalizacion, on_delete=models.CASCADE, db_column='id_personalizacion')
    id_combo = models.ForeignKey(Combo, on_delete=models.CASCADE, db_column='id_combo')
    precio_adicional_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'detalleadicional'

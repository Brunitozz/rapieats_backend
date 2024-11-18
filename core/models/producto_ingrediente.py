from django.db import models
from .producto import Producto
from .producto import Ingrediente

class ProductoIngrediente(models.Model):
    id_producto_ingrediente = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_column='id_producto'
    )
    id_ingrediente = models.ForeignKey(
        Ingrediente,
        on_delete=models.CASCADE,
        db_column='id_ingrediente'
    )
    cantidad = models.IntegerField()
    precio_adicional = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False  
        
        db_table = 'producto_ingrediente'

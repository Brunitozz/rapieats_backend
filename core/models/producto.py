from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'categoria'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = 'producto'


class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, unique=True)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ingrediente'

from django.db import models
from .producto import Producto
from .dispositivo import DispositivoDeAutoservicio
from payments.models import Pago


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=100)
    id_pago = models.ForeignKey(Pago, on_delete=models.CASCADE, db_column='id_pago')
    id_dispositivo = models.ForeignKey(DispositivoDeAutoservicio, on_delete=models.CASCADE, db_column='id_dispositivo')

    class Meta:
        managed = False
        db_table = 'pedido'


class DetallePedido(models.Model):
    id_datallepedido = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, db_column='id_pedido')
    id_detalle_adicional = models.ForeignKey('Personalizacion', on_delete=models.CASCADE, db_column='id_detalle_adicional')
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'detallepedido'

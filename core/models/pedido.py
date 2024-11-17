from django.db import models
from .producto import Producto
from .dispositivo import DispositivoDeAutoservicio
from payments.models import Payment

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=100)
    pago = models.ForeignKey(Payment, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(DispositivoDeAutoservicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.id_pedido} - {self.tipo}"


class DetallePedido(models.Model):
    id_datallepedido = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"DetallePedido {self.id_datallepedido} - Pedido {self.pedido.id_pedido}"

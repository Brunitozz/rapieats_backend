from django.db import models

from django.db import models

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    metodo = models.CharField(max_length=100) 
    monto = models.DecimalField(max_digits=10, decimal_places=2) 
    estado = models.CharField(
        max_length=100,
        choices=[('pendiente', 'Pendiente'), ('completado', 'Completado'), ('fallido', 'Fallido')],
        default='pendiente'
    ) 

    class Meta:
        managed = False  
        db_table = 'pago' 

    def __str__(self):
        return f"Pago #{self.id_pago} - {self.metodo} - {self.estado}"

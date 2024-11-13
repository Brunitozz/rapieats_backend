from django.db import models

# Create your models here.
class Payment(models.Model):
    id_payment = models.AutoField(primary_key=True)
    metod = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.metodo} - {self.monto} ({self.estado})"
     
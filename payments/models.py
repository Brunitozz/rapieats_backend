from django.db import models

class Payment(models.Model):
    id_payment = models.AutoField(primary_key=True)
    method = models.CharField(max_length=100) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.method} - {self.amount} ({self.state})" 
from django.db import models

class DispositivoDeAutoservicio(models.Model):
    id_dispositivo = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ubicacion} - {self.estado}"

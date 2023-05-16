from django.db import models

# Create your models here.

class SuperHeroe(models.Model):
    nombre = models.CharField(max_length=20)
    superpoder = models.CharField(max_length=20)
    motivo = models.TextField()
    autor =  models.CharField(max_length=20)

    def __str__ (self):
        return f"{self.nombre} - {self.superpoder} - {self.motivo} - {self.autor}"
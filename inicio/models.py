from django.db import models

# Create your models here.

class SuperHeroe(models.Model):
    nombre = models.CharField(max_length=20)
    superpoder = models.CharField(max_length=20)
    motivo = models.TextField()
    # edad = models.IntegerField()
    autor =  models.CharField(max_length=20)

    def __str__ (self):
        return f"{self.nombre}"
        # return f"Nombre: {self.nombre} - Super Poder: {self.superpoder} - Motivo: {self.motivo} - Auto: {self.autor}"
    
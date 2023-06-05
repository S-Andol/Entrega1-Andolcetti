from django.db import models
from ckeditor.fields import RichTextField, RichTextFormField

# Create your models here.

class SuperHeroe(models.Model):
    nombre = models.CharField(max_length=20)
    superpoder = models.CharField(max_length=20)
    motivo = RichTextField()
    # edad = models.IntegerField()
    autor =  models.CharField(max_length=20)
    #Falta campo imagen (avatar)

    def __str__ (self):
        return f"{self.nombre}"
        # return f"Nombre: {self.nombre} - Super Poder: {self.superpoder} - Motivo: {self.motivo} - Auto: {self.autor}"
    
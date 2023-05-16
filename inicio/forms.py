# Creamos los formularios
from django import forms

class CreacionSuperHereoFormulario(forms.Form):
    nombre = forms.CharField (max_length=20) 
    superpoder = forms.CharField (max_length=20) 
    motivo = forms.CharField (max_length=20) 
    autor = forms.CharField (max_length=20) 
    
class BuscarSuperHeroe(forms.Form):
    nombre = forms.CharField (max_length=20) 
    autor = forms.CharField (max_length=20) 
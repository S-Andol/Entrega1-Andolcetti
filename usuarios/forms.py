# indicarle cual es el padre siempre al formulario

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class FormularioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
    class Meta:
        model = User
        fields = {'username','email','password1','password2'}
        help_texts = {k: '' for k in fields}
    

class EdicionPerfil(UserChangeForm):
    first_name = forms.CharField(label='Nombre', max_length=30)
    last_name = forms.CharField(label='Apellido', max_length=30)
    password = None
    email = forms.EmailField()
    
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = {'email','first_name','last_name','avatar'}
        
    
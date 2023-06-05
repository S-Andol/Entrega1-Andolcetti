from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from usuarios.forms import FormularioRegistro, EdicionPerfil
from usuarios.models import InfoExtra

# Create your views here.

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
    
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contraseña = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contraseña)
            
            login_django(request, user)
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio:inicio')

        else:
            return render(request, 'usuarios/login.html', {'form': formulario})
        
    formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': formulario})


def registro(request):
    
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
    
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('usuarios:login')

        else:
            return render(request, 'usuarios/registro.html', {'form': formulario})
        
    formulario = FormularioRegistro()
    return render(request, 'usuarios/registro.html', {'form': formulario})

# El decorador se agrega por encima de la funcion y se le agrega un @
@login_required
def editar_perfil(request):
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST,request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('avatar'):
                request.user.infoextra.avatar = formulario.cleaned_data.get('avatar')
                request.user.infoextra.save()
            
            formulario.save()
            
            return redirect('usuarios:editar_perfil')

        else:
            return render(request, 'usuarios/editar_perfil.html', {'form': formulario})
        
    formulario = EdicionPerfil(initial={'avatar':request.user.infoextra.avatar}, instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})



class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_contraseña.html'
    success_url =reverse_lazy('usuarios:editar_perfil')
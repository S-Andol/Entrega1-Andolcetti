from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('registro/', views.registro, name = 'registro'),
    path('perfil/editar/', views.editar_perfil, name = 'editar_perfil'),
    path('perfil/editar/cambiar_contraseña', views.CambiarContraseña.as_view(), name = 'cambiar_contraseña'),
    path('logout/', LogoutView.as_view(template_name = 'usuarios/logout.html'), name='logout')
]

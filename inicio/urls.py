from django.urls import path
from inicio import views

app_name = 'inicio'


urlpatterns = [ 
    
    path ('', views.mi_vista, name = 'inicio'),
    
    path('crear-superheroe/', views.crear_superheroe, name = 'crear_superheroe'),
    path('superheroes/', views.lista_superheroes, name = 'listar_superheroes'),
    path('superheroes/<int:pk>/', views.SuperHeroeDetailView.as_view, name = 'detalle_superheroes'),
    path('superheroes/<int:pk>/modificar/', views.SuperHeroeUpdateView.as_view, name = 'modificar_superheroes'),
    path('superheroes/<int:pk>/eliminar/', views.SuperHeroeDeleteView.as_view , name = 'eliminar_superheroes'),
    path('sobre-mi/', views.sobre_mi, name = 'sobre_mi'),
    

    
]
    # path('crear-superheroe/', views.crear_superheroe, name = 'crear_superheroe'),
    # path('superheroes/<int:pk>/', views.lista_superheroes.as_view, name = 'listar_superheroes'),
    # path('superheroes/<int:pk>/', views.SuperHeroeDetailView, name = 'detalle_superheroes'),
    # path('superheroes/<int:pk>/modificar/', views.SuperHeroeUpdateView.as_view, name = 'modificar_superheroes'),
    # path('superheroes/<int:pk>/eliminar/', views.SuperHeroeDeleteView , name = 'eliminar_superheroes'),
    # path('sobre-mi/', views.sobre_mi, name = 'sobre_mi'),
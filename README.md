# Entrega1-Andolcetti

Abro terminal y colocamos pwd

# Clonamos los archivos del GitHub
    git clone https://github.com/S-Andol/Proyecto_Django.git

# Salimos de VSC y lo abrimos pero desde nuestra carpeta recien creada

# Al bajarnos los archivos con el git clone, automaticamente se hace el git init.

# Creamos un entorno virtual

python -m venv venv
    Al tener en .gitignore de las extenciones el formato .venv. Significa que no le va a dar bola a nuestra carpeta. No las va a tener en cuenta ni las va a subir a la nube.

Si hay alguna carpeta que queres que se ignore o no se suba. HAY QUE IGNORARLO ANTES DE "CREARLO" AL ARCHIVO!!!

# Activamos el entorno virtual

. venv/Scripts/activate

pip = manejador de paquetes en python

# Mostrar los paquetes que tengo instalado en el entorno virtual que se creo

pip freeze

# Instalamos los paquetes

pip install Django

# Revisamos nuevamente los paquetes instalados

pip freeze

# Para poder utilizar los paquetes que voy agregando a venv, hay que utlizar un archivo aparte. "requirements.txt

pip freeze > requirements.txt
Crea el archivo y agrega todos los paquetes instalados...

# Habilitamos un comando de Django

django-admin startproject "nombre del proyecto"(no utilizar "-"Pero si se puede "_")
django-admin startproject proyecto_django

# Ahora tenemos que colocar al mismo nivel que los .gitingore, README y requiments.

Cambiamos el nombre de la carpeta de afuera "proyecto_django" por "proyecto_django2"
Sacamos tanto la carpeta interna "proyecto_django" y "manage.py"

Estructura:
    proyecto_django
    venv
    .gitignore
    manage.py
    README.md
    requirements.txt

# Probamos el archivo manage.py, ejecutando el server

python manage.py runserver

Nos lanza una URL, donde por medio de esa direccion se puede acceder al proyecto. http://127.0.0.1:8000/

Al correr el runserve se crea un archivo: 
db.sqlite3, es un archivo de base de datos. (el cual me lo ignora)

asgi.py y wsgi.py son archivos que indican la forma en que se van a conectar la gente con el proyecto.

settings.py tiene casi todas las config del proyecto

urls.py tiene las direcciones por donde nos vamos a dirigir a nuestras paginas

# Migrar a la base de datos archivos, para que ande correctamente.

python manage.py migrate
Si entramos en db.sqlite3 podemos observar las 18 migraciones...

# git status

# git add .

# git commit -m "Primeros pasos"

# git status

# git push (lo subimos)


# A modo de muestra:
    # Creamos en urls.py un camino - path

    path("van argumentos") 
    path('',"vista"),
    Agregamos:
    path('',mi_vista),

    # Agregamos un nuevo archivo dentro de "proyecto_django"

    Creamos views.py y escribimos dentro una funcion.

    def mi_vista(request):
        return ...
    
    # Creamos el import para llamarlo
        
        Creamos dentro de urls.py
            from proyecto_django.views import mi_vista

    # Traemos un httpResponse a mi_vista
        
        Agregamos arriba de la funcion def...

        from django.http import HttpResponse

        y modificamos el return...

        def mi_vista(request):
            return HttpResponse('<h1>Mi Primera Vista</h1>')


1:36:00

# Final

git add .
git status
git commit -m "Cierre Clase 1 Django"
git push
FINAL


# RECORDAR AL INICIAR
. venv/Script/activate
y de ser necesario...
python manage.py migrate


1:07

# SUPER USUARIO 
Creamos un super usuario para poder modificar cosas

python manage.py createsuperuser

usuario: admin
email: sergio.andol@gmail.com
password: 1234
Bypass password validation and create user anyway? [y/N]: y

# Recordar tirar el runserver porque sino no me va a aparecer el http://127.0.0.1:8000/admin/login/?next=/admin/

Desde esa pagina vamos a poder editar todo lo que nosotros configuremos en nuestra app.


# vamos al admin
Colocamos:

from inicio.models import Animal, Persona

admin.site.register(Animal)
admin.site.register(Persona)

De esta manera lo vamos a poder modificar tras bambalinas (?)



# RECORDAR AL INICIAR
. venv/Scripts/activate
y de ser necesario...
python manage.py migrate

# Cuando Modificamos algo en models
Terminamos de modificar y colocamos por pantalla
python manage.py makemigrations
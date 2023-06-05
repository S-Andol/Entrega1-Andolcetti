from django.contrib import admin
from inicio.models import SuperHeroe
from usuarios.models import InfoExtra

# Register your models here.

admin.site.register(SuperHeroe)
admin.site.register(InfoExtra)
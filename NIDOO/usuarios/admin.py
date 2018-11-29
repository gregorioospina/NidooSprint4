from django.contrib import admin
from . models import Usuario, Parqueadero, Capacidad

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Parqueadero)
admin.site.register(Capacidad)
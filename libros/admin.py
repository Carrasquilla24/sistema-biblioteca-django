
from django.contrib import admin
from .models import Categoria, Libro, Lector, Prestamo

admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Prestamo)

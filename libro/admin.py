from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'categoria', 'cantidad_disponible', 'cantidad_total')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('categoria', 'año_publicacion', 'editorial')
    readonly_fields = ('fecha_agregado',)
    fieldsets = (
        ('Información Bibliográfica', {
            'fields': ('titulo', 'autor', 'isbn', 'editorial', 'año_publicacion', 'num_paginas')
        }),
        ('Disponibilidad', {
            'fields': ('categoria', 'cantidad_total', 'cantidad_disponible', 'precio')
        }),
        ('Descripción', {
            'fields': ('descripcion',)
        }),
        ('Auditoría', {
            'fields': ('fecha_agregado',),
            'classes': ('collapse',)
        }),
    )

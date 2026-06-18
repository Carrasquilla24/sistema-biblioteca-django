from django.contrib import admin
from .models import Lector

@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'correo', 'estado')
    search_fields = ('nombre', 'apellido', 'cedula', 'correo')
    list_filter = ('estado', 'ciudad', 'fecha_registro')
    readonly_fields = ('fecha_registro',)
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'cedula')
        }),
        ('Contacto', {
            'fields': ('correo', 'telefono', 'direccion', 'ciudad')
        }),
        ('Estado', {
            'fields': ('estado',)
        }),
        ('Auditoría', {
            'fields': ('fecha_registro',),
            'classes': ('collapse',)
        }),
    )

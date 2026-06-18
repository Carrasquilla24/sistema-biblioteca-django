from django.contrib import admin
from .models import Prestamo

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('libro', 'lector', 'fecha_prestamo', 'fecha_devolucion_esperada', 'estado', 'multa')
    search_fields = ('libro__titulo', 'lector__nombre', 'lector__apellido')
    list_filter = ('estado', 'fecha_prestamo', 'fecha_devolucion_esperada')
    readonly_fields = ('fecha_prestamo',)
    fieldsets = (
        ('Información del Préstamo', {
            'fields': ('libro', 'lector', 'fecha_prestamo')
        }),
        ('Devolución', {
            'fields': ('fecha_devolucion_esperada', 'fecha_devolucion_real')
        }),
        ('Estado y Multa', {
            'fields': ('estado', 'multa')
        }),
        ('Observaciones', {
            'fields': ('notas',)
        }),
    )

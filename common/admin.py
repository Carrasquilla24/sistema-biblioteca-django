from django.contrib import admin
from .models import Configuracion

@admin.register(Configuracion)
class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ('nombre_biblioteca', 'dias_prestamo', 'multa_por_dia')
    fieldsets = (
        ('Información General', {
            'fields': ('nombre_biblioteca', 'correo_contacto', 'telefono', 'direccion')
        }),
        ('Política de Préstamos', {
            'fields': ('dias_prestamo', 'multa_por_dia')
        }),
    )
    
    def has_add_permission(self, request):
        # Permitir solo una configuración
        return not Configuracion.objects.exists()

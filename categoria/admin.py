from django.contrib import admin
from .models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    search_fields = ('nombre',)
    list_filter = ('fecha_creacion',)
    readonly_fields = ('fecha_creacion',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion')
        }),
        ('Auditoría', {
            'fields': ('fecha_creacion',),
            'classes': ('collapse',)
        }),
    )

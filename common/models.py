from django.db import models

class ModeloBase(models.Model):
    """Modelo base para todas las entidades"""
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        abstract = True


class Configuracion(models.Model):
    """Configuración general de la biblioteca"""
    nombre_biblioteca = models.CharField(max_length=200, default='Sistema Biblioteca')
    dias_prestamo = models.IntegerField(default=14)
    multa_por_dia = models.DecimalField(max_digits=10, decimal_places=2, default=5000)
    correo_contacto = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    
    class Meta:
        verbose_name = 'Configuración'
        verbose_name_plural = 'Configuraciones'
    
    def __str__(self):
        return self.nombre_biblioteca


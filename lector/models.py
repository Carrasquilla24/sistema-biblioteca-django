from django.db import models

class Lector(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20, unique=True)
    direccion = models.TextField()
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('activo', 'Activo'),
            ('inactivo', 'Inactivo'),
            ('suspendido', 'Suspendido')
        ],
        default='activo'
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'
        ordering = ['apellido', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


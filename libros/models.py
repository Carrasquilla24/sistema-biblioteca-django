
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Lector(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)

    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)

    estado = models.CharField(
        max_length=20,
        choices=[
            ('prestado', 'Prestado'),
            ('devuelto', 'Devuelto'),
            ('atrasado', 'Atrasado')
        ],
        default='prestado'
    )

    def __str__(self):
        return f"{self.libro} - {self.lector}"

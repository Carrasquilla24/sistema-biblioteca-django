from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Lector(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    disponible = models.BooleanField(default=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='libros'
    )

    def __str__(self):
        return self.titulo


class Prestamo(models.Model):

    ESTADOS = [
        ('Prestado', 'Prestado'),
        ('Devuelto', 'Devuelto'),
        ('Atrasado', 'Atrasado'),
    ]

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name='prestamos'
    )

    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE,
        related_name='prestamos'
    )

    fecha_prestamo = models.DateField()
    fecha_entrega = models.DateField()
    fecha_devolucion = models.DateField(
        null=True,
        blank=True
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Prestado'
    )

    def __str__(self):
        return f"{self.libro} - {self.lector}"
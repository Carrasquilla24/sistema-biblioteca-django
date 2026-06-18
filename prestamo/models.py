from django.db import models
from datetime import timedelta
from django.utils import timezone
from libro.models import Libro
from lector.models import Lector

class Prestamo(models.Model):
    ESTADO_CHOICES = [
        ('prestado', 'Prestado'),
        ('devuelto', 'Devuelto'),
        ('atrasado', 'Atrasado'),
        ('cancelado', 'Cancelado')
    ]
    
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion_esperada = models.DateField()
    fecha_devolucion_real = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='prestado')
    multa = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notas = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'
        ordering = ['-fecha_prestamo']
    
    def __str__(self):
        return f"{self.libro} - {self.lector}"
    
    def dias_atraso(self):
        if self.estado == 'prestado':
            return (timezone.now().date() - self.fecha_devolucion_esperada).days
        return 0
    
    def calcular_multa(self):
        dias = self.dias_atraso()
        if dias > 0:
            self.multa = dias * 5000  # 5000 pesos por día
        return self.multa


from django.db import models
from categoria.models import Categoria

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    editorial = models.CharField(max_length=100)
    año_publicacion = models.IntegerField()
    num_paginas = models.IntegerField()
    cantidad_total = models.IntegerField(default=1)
    cantidad_disponible = models.IntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']
    
    def __str__(self):
        return self.titulo
    
    def disponible(self):
        return self.cantidad_disponible > 0


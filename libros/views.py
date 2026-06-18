from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from libro.models import Libro

class LibrosListView(View):
    """Vista para listar todos los libros en formato JSON"""
    def get(self, request):
        libros = Libro.objects.all().values('id', 'titulo', 'autor', 'isbn', 'categoria__nombre', 'cantidad_disponible')
        return JsonResponse({
            'status': 'success',
            'count': len(libros),
            'libros': list(libros)
        })

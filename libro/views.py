from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Libro
from .forms import LibroForm

class ListaLibros(View):
    def get(self, request):
        libros = Libro.objects.all()
        categoria_filtro = request.GET.get('categoria')
        if categoria_filtro:
            libros = libros.filter(categoria_id=categoria_filtro)
        return render(request, 'libro/lista.html', {'libros': libros})

class CrearLibro(View):
    def get(self, request):
        form = LibroForm()
        return render(request, 'libro/form.html', {'form': form})
    
    def post(self, request):
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro agregado exitosamente')
            return redirect('libro_lista')
        return render(request, 'libro/form.html', {'form': form})

class EditarLibro(View):
    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        form = LibroForm(instance=libro)
        return render(request, 'libro/form.html', {'form': form, 'libro': libro})
    
    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado exitosamente')
            return redirect('libro_lista')
        return render(request, 'libro/form.html', {'form': form, 'libro': libro})

class EliminarLibro(View):
    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente')
        return redirect('libro_lista')

class DetallesLibro(View):
    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        prestamos = libro.prestamo_set.all().order_by('-fecha_prestamo')
        return render(request, 'libro/detalles.html', {'libro': libro, 'prestamos': prestamos})

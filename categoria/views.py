from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Categoria
from .forms import CategoriaForm

class ListaCategorias(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, 'categoria/lista.html', {'categorias': categorias})

class CrearCategoria(View):
    def get(self, request):
        form = CategoriaForm()
        return render(request, 'categoria/form.html', {'form': form})
    
    def post(self, request):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente')
            return redirect('categoria_lista')
        return render(request, 'categoria/form.html', {'form': form})

class EditarCategoria(View):
    def get(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        form = CategoriaForm(instance=categoria)
        return render(request, 'categoria/form.html', {'form': form, 'categoria': categoria})
    
    def post(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente')
            return redirect('categoria_lista')
        return render(request, 'categoria/form.html', {'form': form, 'categoria': categoria})

class EliminarCategoria(View):
    def post(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente')
        return redirect('categoria_lista')

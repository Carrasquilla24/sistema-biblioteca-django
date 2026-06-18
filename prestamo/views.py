from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.utils import timezone
from .models import Prestamo
from .forms import PrestamoForm

class ListaPrestamos(View):
    def get(self, request):
        prestamos = Prestamo.objects.all()
        estado_filtro = request.GET.get('estado')
        if estado_filtro:
            prestamos = prestamos.filter(estado=estado_filtro)
        return render(request, 'prestamo/lista.html', {'prestamos': prestamos})

class CrearPrestamo(View):
    def get(self, request):
        form = PrestamoForm()
        return render(request, 'prestamo/form.html', {'form': form})
    
    def post(self, request):
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save()
            prestamo.libro.cantidad_disponible -= 1
            prestamo.libro.save()
            messages.success(request, 'Préstamo registrado exitosamente')
            return redirect('prestamo_lista')
        return render(request, 'prestamo/form.html', {'form': form})

class EditarPrestamo(View):
    def get(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        form = PrestamoForm(instance=prestamo)
        return render(request, 'prestamo/form.html', {'form': form, 'prestamo': prestamo})
    
    def post(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Préstamo actualizado exitosamente')
            return redirect('prestamo_lista')
        return render(request, 'prestamo/form.html', {'form': form, 'prestamo': prestamo})

class DevolverLibro(View):
    def post(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        prestamo.fecha_devolucion_real = timezone.now().date()
        prestamo.estado = 'devuelto'
        prestamo.calcular_multa()
        prestamo.save()
        prestamo.libro.cantidad_disponible += 1
        prestamo.libro.save()
        messages.success(request, 'Libro devuelto exitosamente')
        return redirect('prestamo_lista')

class DetallesPrestamo(View):
    def get(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        return render(request, 'prestamo/detalles.html', {'prestamo': prestamo})

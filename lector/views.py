from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Lector
from .forms import LectorForm

class ListaLectores(View):
    def get(self, request):
        lectores = Lector.objects.all()
        estado_filtro = request.GET.get('estado')
        if estado_filtro:
            lectores = lectores.filter(estado=estado_filtro)
        return render(request, 'lector/lista.html', {'lectores': lectores})

class CrearLector(View):
    def get(self, request):
        form = LectorForm()
        return render(request, 'lector/form.html', {'form': form})
    
    def post(self, request):
        form = LectorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lector registrado exitosamente')
            return redirect('lector_lista')
        return render(request, 'lector/form.html', {'form': form})

class EditarLector(View):
    def get(self, request, pk):
        lector = get_object_or_404(Lector, pk=pk)
        form = LectorForm(instance=lector)
        return render(request, 'lector/form.html', {'form': form, 'lector': lector})
    
    def post(self, request, pk):
        lector = get_object_or_404(Lector, pk=pk)
        form = LectorForm(request.POST, instance=lector)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lector actualizado exitosamente')
            return redirect('lector_lista')
        return render(request, 'lector/form.html', {'form': form, 'lector': lector})

class EliminarLector(View):
    def post(self, request, pk):
        lector = get_object_or_404(Lector, pk=pk)
        lector.delete()
        messages.success(request, 'Lector eliminado exitosamente')
        return redirect('lector_lista')

class DetallesLector(View):
    def get(self, request, pk):
        lector = get_object_or_404(Lector, pk=pk)
        prestamos = lector.prestamo_set.all()
        return render(request, 'lector/detalles.html', {'lector': lector, 'prestamos': prestamos})

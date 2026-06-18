from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'lector', 'fecha_devolucion_esperada', 'estado', 'notas']
        widgets = {
            'libro': forms.Select(attrs={'class': 'form-control'}),
            'lector': forms.Select(attrs={'class': 'form-control'}),
            'fecha_devolucion_esperada': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notas', 'rows': 2}),
        }

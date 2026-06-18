from django import forms
from .models import Lector

class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = ['nombre', 'apellido', 'cedula', 'correo', 'telefono', 'direccion', 'ciudad', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dirección', 'rows': 2}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

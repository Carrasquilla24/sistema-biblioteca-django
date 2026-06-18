from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'isbn', 'editorial', 'año_publicacion', 'num_paginas', 
                  'cantidad_total', 'cantidad_disponible', 'precio', 'descripcion', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del libro'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Editorial'}),
            'año_publicacion': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'num_paginas': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'cantidad_total': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'cantidad_disponible': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'step': '0.01'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

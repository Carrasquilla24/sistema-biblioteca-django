from django.urls import path
from .views import ListaPrestamos, CrearPrestamo, EditarPrestamo, DevolverLibro, DetallesPrestamo

urlpatterns = [
    path('', ListaPrestamos.as_view(), name='prestamo_lista'),
    path('crear/', CrearPrestamo.as_view(), name='prestamo_crear'),
    path('<int:pk>/editar/', EditarPrestamo.as_view(), name='prestamo_editar'),
    path('<int:pk>/devolver/', DevolverLibro.as_view(), name='prestamo_devolver'),
    path('<int:pk>/detalles/', DetallesPrestamo.as_view(), name='prestamo_detalles'),
]

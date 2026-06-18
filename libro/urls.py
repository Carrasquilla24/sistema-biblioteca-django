from django.urls import path
from .views import ListaLibros, CrearLibro, EditarLibro, EliminarLibro, DetallesLibro

urlpatterns = [
    path('', ListaLibros.as_view(), name='libro_lista'),
    path('crear/', CrearLibro.as_view(), name='libro_crear'),
    path('<int:pk>/editar/', EditarLibro.as_view(), name='libro_editar'),
    path('<int:pk>/eliminar/', EliminarLibro.as_view(), name='libro_eliminar'),
    path('<int:pk>/detalles/', DetallesLibro.as_view(), name='libro_detalles'),
]

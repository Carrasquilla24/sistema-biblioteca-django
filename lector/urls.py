from django.urls import path
from .views import ListaLectores, CrearLector, EditarLector, EliminarLector, DetallesLector

urlpatterns = [
    path('', ListaLectores.as_view(), name='lector_lista'),
    path('crear/', CrearLector.as_view(), name='lector_crear'),
    path('<int:pk>/editar/', EditarLector.as_view(), name='lector_editar'),
    path('<int:pk>/eliminar/', EliminarLector.as_view(), name='lector_eliminar'),
    path('<int:pk>/detalles/', DetallesLector.as_view(), name='lector_detalles'),
]

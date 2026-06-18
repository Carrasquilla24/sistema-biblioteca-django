from django.urls import path
from .views import ListaCategorias, CrearCategoria, EditarCategoria, EliminarCategoria

urlpatterns = [
    path('', ListaCategorias.as_view(), name='categoria_lista'),
    path('crear/', CrearCategoria.as_view(), name='categoria_crear'),
    path('<int:pk>/editar/', EditarCategoria.as_view(), name='categoria_editar'),
    path('<int:pk>/eliminar/', EliminarCategoria.as_view(), name='categoria_eliminar'),
]

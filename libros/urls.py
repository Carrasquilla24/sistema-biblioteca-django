from django.urls import path
from .views import LibrosListView

urlpatterns = [
    path('api/', LibrosListView.as_view(), name='libros_api'),
]

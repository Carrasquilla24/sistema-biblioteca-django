
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('categoria/', include('categoria.urls')),
    path('lector/', include('lector.urls')),
    path('libro/', include('libro.urls')),
    path('libros/', include('libros.urls')),
    path('prestamo/', include('prestamo.urls')),
]

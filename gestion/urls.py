from django.urls import path
from django.views.generic import RedirectView
from .views import (
    AutorListView,
    AutorCreateView,
    AutorUpdateView,
    AutorDeleteView,
    LibroListView,
    LibroCreateView,
    LibroUpdateView,
    LibroDeleteView,
)

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='lista_autores', permanent=False)),
    path('autores/', AutorListView.as_view(), name='lista_autores'),
    path('autores/crear/', AutorCreateView.as_view(), name='crear_autor'),
    path('autores/<int:pk>/editar/', AutorUpdateView.as_view(), name='editar_autor'),
    path('autores/<int:pk>/eliminar/', AutorDeleteView.as_view(), name='eliminar_autor'),
    path('libros/', LibroListView.as_view(), name='lista_libros'),
    path('libros/crear/', LibroCreateView.as_view(), name='crear_libro'),
    path('libros/<int:pk>/editar/', LibroUpdateView.as_view(), name='editar_libro'),
    path('libros/<int:pk>/eliminar/', LibroDeleteView.as_view(), name='eliminar_libro'),
]

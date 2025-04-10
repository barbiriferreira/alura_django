from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),  # URL para la página de inicio
    path('imagem/', imagem, name='imagem')  # URL para la galería de imágenes
]

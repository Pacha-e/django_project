from django.urls import path
from .views import crear_usuario

# Lista de URLs de esta aplicación
urlpatterns = [
    # Ruta raíz de la app: http://localhost:8000/
    path('', crear_usuario, name='crear_usuario'),
]
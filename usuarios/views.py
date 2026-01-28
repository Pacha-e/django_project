from django.shortcuts import render, redirect
from .models import Usuario

# Vista principal: crear usuario
def crear_usuario(request):
    """
    Esta función maneja dos cosas:
    1. GET: Mostrar el formulario vacío
    2. POST: Guardar el usuario y recargar
    """
    
    # Verificar si el usuario envió el formulario (método POST)
    if request.method == 'POST':
        # Obtener el nombre del formulario
        # request.POST es un diccionario con los datos enviados
        nombre = request.POST.get('nombre_usuario')
        
        # Crear y guardar el usuario en la base de datos
        Usuario.objects.create(nombre_usuario=nombre)
        
        # Redirigir a la misma página (recarga limpia)
        return redirect('crear_usuario')
    
    # Si es método GET (primera carga), mostrar el formulario
    return render(request, 'usuarios/formulario.html')
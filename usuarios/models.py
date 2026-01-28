from django.db import models

# Este es nuestro modelo Usuario
# Django lo convertirá automáticamente en una tabla en PostgreSQL
class Usuario(models.Model):
    # Campo: nombre_usuario
    # CharField = campo de texto
    # max_length=100 = máximo 100 caracteres
    nombre_usuario = models.CharField(max_length=100)
    
    # Este método se ejecuta cuando imprimes un objeto Usuario
    # Ejemplo: print(usuario) mostrará el nombre
    def __str__(self):
        return self.nombre_usuario
    
    # Metadata opcional (personalización)
    class Meta:
        verbose_name = "Usuario"           # Nombre singular en admin
        verbose_name_plural = "Usuarios"   # Nombre plural en admin
        ordering = ['-id']                 # Ordenar por ID descendente (más recientes primero)
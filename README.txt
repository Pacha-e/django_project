# Proyecto Django: Registro de Usuarios con PostgreSQL

## Descripción del Proyecto
Aplicación web desarrollada con Django y PostgreSQL que permite el registro de usuarios a través de un formulario web, almacenando los datos en una base de datos relacional.

**Objetivo de la tarea**: Aprender a configurar Django con PostgreSQL y crear una interfaz funcional para gestión de datos.

## Características Implementadas
- Formulario web para registro de usuarios
- Conexión a base de datos PostgreSQL
- Modelo de datos `Usuario` con campo `nombre_usuario`
- Migraciones de base de datos automatizadas
- Interfaz minimalista y funcional
- Evidencias de funcionamiento (capturas de pantalla)

## Tecnologías Utilizadas
- **Backend**: Python 3.x, Django 4.x
- **Base de datos**: PostgreSQL
- **Driver**: psycopg2-binary
- **Frontend**: HTML5
- **Control de versiones**: Git & GitHub

## Estructura del Proyecto
django_project/
├── usuario_project/     # Configuración principal de Django
│   ├── __init__.py
│   ├── settings.py     # Configuración de PostgreSQL
│   ├── urls.py         # Rutas principales
│   └── wsgi.py
├── usuarios/           # Aplicación de usuarios
│   ├── migrations/     # Migraciones de base de datos
│   ├── templates/      # Plantilla HTML
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py       # Modelo Usuario
│   ├── tests.py
│   └── views.py        # Lógica del formulario
├── screenshots/        # Evidencias de funcionamiento
│   ├── formulario.png
│   ├── base_datos.png
│   └── (otras capturas)
├── manage.py           # Script de administración
├── requirements.txt    # Dependencias del proyecto
└── .gitignore          # Archivos excluidos de Git

## Instalación y Configuración

### Prerrequisitos
- Python 3.10 o superior
- PostgreSQL instalado y en ejecución
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   git clone https://github.com/Pacha-e/django_project.git
   cd django_project

2. **Crear y activar entorno virtual**
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate

3. **Instalar dependencias**
   pip install django psycopg2-binary

4. **Configurar base de datos PostgreSQL**
   -- Ejecutar en psql o pgAdmin
   CREATE DATABASE usuarios_db;
   CREATE USER usuario_django WITH PASSWORD 'password123';
   GRANT ALL PRIVILEGES ON DATABASE usuarios_db TO usuario_django;

5. **Configurar conexión a base de datos**
   En `usuario_project/settings.py`, verificar:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'usuarios_db',
           'USER': 'usuario_django',
           'PASSWORD': 'password123',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }

6. **Aplicar migraciones**
   python manage.py makemigrations
   python manage.py migrate

7. **Crear superusuario (opcional)**
   python manage.py createsuperuser

8. **Ejecutar servidor de desarrollo**
   python manage.py runserver

9. **Acceder a la aplicación**
   - Formulario de registro: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## Uso de la Aplicación

### Registro de Usuarios
1. Acceder a http://127.0.0.1:8000/
2. Ingresar nombre de usuario en el campo de texto
3. Hacer clic en "Guardar"
4. El usuario se almacenará en la base de datos PostgreSQL

### Verificación de Datos
Para verificar que los datos se guardaron correctamente:

**Opción 1: Usar psql**
psql -U usuario_django -d usuarios_db -c "SELECT * FROM usuarios_usuario;"

**Opción 2: Panel de administración Django**
1. Acceder a http://127.0.0.1:8000/admin/
2. Iniciar sesión con el superusuario creado
3. Navegar a la sección "Usuarios"

## Evidencias de Funcionamiento

### Capturas de Pantalla Incluidas
En la carpeta `screenshots/` se encuentran:

1. **formulario.png** - Interfaz del formulario en funcionamiento
2. **base_datos.png** - Consulta SQL mostrando los registros en PostgreSQL
3. **django_admin.png** - Vista del panel de administración de Django

### Verificación de Conexión a PostgreSQL
-- Consulta para verificar conexión
SELECT 
    table_name, 
    column_name, 
    data_type 
FROM information_schema.columns 
WHERE table_name = 'usuarios_usuario';

## Solución de Problemas Comunes

### Error: "No se puede conectar al servidor PostgreSQL"
- Verificar que PostgreSQL esté en ejecución
- Confirmar credenciales en settings.py
- Revisar que el usuario tenga permisos sobre la base de datos

### Error: "ModuleNotFoundError: No module named 'psycopg2'"
pip install psycopg2-binary

### Error: "relation 'usuarios_usuario' does not exist"
python manage.py makemigrations usuarios
python manage.py migrate

## Estructura de la Base de Datos

### Tabla: usuarios_usuario
| Columna | Tipo | Descripción |
|---------|------|-------------|
| id | SERIAL (PK) | Identificador único autoincremental |
| nombre_usuario | VARCHAR(100) | Nombre del usuario registrado |

### Creación mediante migraciones Django
# usuarios/models.py
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_usuario

## Comandos Git Utilizados
# Inicialización y subida del proyecto
git init
git add .
git commit -m "Proyecto Django: registro de usuario"
git branch -M main
git remote add origin https://github.com/Pacha-e/django_project.git
git push -u origin main

## Posibles Mejoras (Extras Opcionales)
1. Validación de campo no vacío en el formulario
2. Listado de usuarios registrados
3. Estilos CSS personalizados
4. Validación de nombres de usuario únicos
5. Paginación de resultados

## Licencia
Este proyecto fue desarrollado como parte de una tarea académica.

## Contacto
- **Repositorio**: https://github.com/Pacha-e/django_project
- **Propósito**: Aprendizaje de Django con PostgreSQL

---

**Nota**: Este proyecto requiere PostgreSQL instalado y configurado localmente. Las credenciales de la base de datos pueden modificarse en `usuario_project/settings.py` según el entorno de despliegue.
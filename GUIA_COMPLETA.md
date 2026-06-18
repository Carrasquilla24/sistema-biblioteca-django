# 📚 Sistema de Biblioteca Django

Sistema completo de gestión de biblioteca desarrollado en Django. Permite administrar libros, categorías, lectores y préstamos de forma eficiente.

## 🎯 Características

- **📖 Gestión de Libros**: Crear, editar, eliminar y consultar libros
- **🏷️ Categorías**: Organizar libros por categorías
- **👥 Lectores**: Registrar y administrar lectores de la biblioteca
- **📤 Préstamos**: Control de préstamos, devoluciones y multas
- **⚙️ Panel Admin**: Interfaz Django admin completa
- **📊 Dashboard**: Panel de inicio con estadísticas

## 📁 Estructura de Carpetas

```
sistema_biblioteca_django/
├── biblioteca/              # Configuración principal
│   ├── settings.py         # Configuración de Django
│   ├── urls.py            # URLs principales
│   └── wsgi.py
├── categoria/             # App de categorías
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── forms.py
│   ├── urls.py
│   └── apps.py
├── lector/                # App de lectores
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── forms.py
│   ├── urls.py
│   └── apps.py
├── libro/                 # App de libros
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── forms.py
│   ├── urls.py
│   └── apps.py
├── prestamo/              # App de préstamos
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── forms.py
│   ├── urls.py
│   └── apps.py
├── common/                # App común (configuración general)
│   ├── models.py
│   ├── admin.py
│   └── apps.py
├── libros/                # App de gestión general
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── apps.py
├── templates/             # Plantillas HTML
│   ├── base.html
│   ├── index.html
│   ├── categoria/
│   ├── lector/
│   ├── libro/
│   └── prestamo/
├── manage.py
└── db.sqlite3
```

## 🚀 Instalación y Configuración

### 1. Crear un entorno virtual
```bash
python -m venv venv
```

### 2. Activar el entorno virtual
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install django
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Crear un superusuario (admin)
```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor
```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000`

## 📋 Modelos Principales

### Categoría
- **nombre**: Nombre de la categoría
- **descripcion**: Descripción opcional
- **fecha_creacion**: Fecha de creación automática

### Lector
- **nombre, apellido**: Nombres del lector
- **cedula**: Identificación única
- **correo**: Email del lector
- **telefono**: Teléfono de contacto
- **direccion**: Dirección del lector
- **ciudad**: Ciudad de residencia
- **estado**: Activo/Inactivo/Suspendido
- **fecha_registro**: Fecha de registro

### Libro
- **titulo**: Título del libro
- **autor**: Autor del libro
- **isbn**: ISBN único
- **editorial**: Editorial
- **año_publicacion**: Año de publicación
- **num_paginas**: Número de páginas
- **cantidad_total**: Cantidad total de libros
- **cantidad_disponible**: Cantidad disponible para préstamo
- **precio**: Precio del libro
- **categoria**: Relación con Categoría
- **descripcion**: Descripción del libro
- **fecha_agregado**: Fecha de agregado

### Préstamo
- **libro**: Libro prestado (FK)
- **lector**: Lector que toma el préstamo (FK)
- **fecha_prestamo**: Fecha del préstamo
- **fecha_devolucion_esperada**: Fecha esperada de devolución
- **fecha_devolucion_real**: Fecha real de devolución
- **estado**: Prestado/Devuelto/Atrasado/Cancelado
- **multa**: Monto de la multa por atraso
- **notas**: Observaciones

## 🔗 URLs Disponibles

### Categorías
- `GET /categoria/` - Listar categorías
- `GET /categoria/crear/` - Crear categoría
- `POST /categoria/crear/` - Guardar categoría
- `GET /categoria/<id>/editar/` - Editar categoría
- `POST /categoria/<id>/editar/` - Guardar cambios
- `POST /categoria/<id>/eliminar/` - Eliminar categoría

### Lectores
- `GET /lector/` - Listar lectores
- `GET /lector/crear/` - Crear lector
- `POST /lector/crear/` - Guardar lector
- `GET /lector/<id>/editar/` - Editar lector
- `GET /lector/<id>/detalles/` - Ver detalles
- `POST /lector/<id>/eliminar/` - Eliminar lector

### Libros
- `GET /libro/` - Listar libros
- `GET /libro/crear/` - Crear libro
- `POST /libro/crear/` - Guardar libro
- `GET /libro/<id>/editar/` - Editar libro
- `GET /libro/<id>/detalles/` - Ver detalles
- `POST /libro/<id>/eliminar/` - Eliminar libro

### Préstamos
- `GET /prestamo/` - Listar préstamos
- `GET /prestamo/crear/` - Crear préstamo
- `POST /prestamo/crear/` - Guardar préstamo
- `GET /prestamo/<id>/editar/` - Editar préstamo
- `POST /prestamo/<id>/devolver/` - Registrar devolución
- `GET /prestamo/<id>/detalles/` - Ver detalles

### Admin
- `/admin/` - Panel administrativo de Django

## 🎨 Características de las Vistas

### Vistas de Listas
- Muestra todos los registros en tablas responsivas
- Opciones de filtrado
- Botones de acción (editar, eliminar, detalles)

### Vistas de Formularios
- Formularios con validación
- Diseño responsive con Bootstrap
- Mensajes de éxito/error

### Vistas de Detalles
- Información completa del registro
- Historial relacionado
- Enlaces de navegación

## 💾 Comandos Útiles

```bash
# Crear nuevas migraciones después de cambiar modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar pruebas
python manage.py test

# Ver las migraciones
python manage.py showmigrations

# Entrar a la consola interactiva
python manage.py shell
```

## 🛠️ Configuración de Email (Opcional)

En `biblioteca/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_email@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_contraseña'
```

## 📝 Ejemplo de Uso en Shell

```python
python manage.py shell

# Crear una categoría
from categoria.models import Categoria
Categoria.objects.create(nombre='Ficción', descripcion='Libros de ficción')

# Crear un lector
from lector.models import Lector
Lector.objects.create(
    nombre='Juan',
    apellido='Pérez',
    cedula='123456789',
    correo='juan@email.com',
    telefono='3001234567',
    direccion='Calle 1 #2-3',
    ciudad='Bogotá'
)

# Crear un libro
from libro.models import Libro
from categoria.models import Categoria
categoria = Categoria.objects.first()
Libro.objects.create(
    titulo='Don Quijote',
    autor='Miguel de Cervantes',
    isbn='978-8499755922',
    editorial='Planeta',
    año_publicacion=1605,
    num_paginas=1000,
    categoria=categoria,
    precio=25.99,
    cantidad_total=5
)

# Crear un préstamo
from prestamo.models import Prestamo
from datetime import timedelta
from django.utils import timezone

libro = Libro.objects.first()
lector = Lector.objects.first()
fecha_devolucion = timezone.now().date() + timedelta(days=14)

Prestamo.objects.create(
    libro=libro,
    lector=lector,
    fecha_devolucion_esperada=fecha_devolucion
)
```

## 🔐 Seguridad

- `DEBUG = True` solo en desarrollo
- Cambiar `SECRET_KEY` en producción
- Usar variables de entorno para datos sensibles
- CSRF protection habilitado
- SQL Injection protection (ORM de Django)

## 📦 Dependencias

- Django 4.2+
- Python 3.8+
- SQLite3 (incluido en Django)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

## 👨‍💻 Autor

Sistema de Biblioteca Django 2026

---

**Nota:** Este es un proyecto educativo. Para producción, se recomienda:
- Usar una base de datos más robusta (PostgreSQL)
- Implementar autenticación y autorización
- Agregar logging
- Implementar caché
- Usar celery para tareas asincrónicas
- Escribir pruebas unitarias

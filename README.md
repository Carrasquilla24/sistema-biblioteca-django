Sistema de Biblioteca Django


Sistema web desarrollado con Python y Django para la gestión y administración de una biblioteca. El proyecto permite registrar libros, gestionar usuarios y controlar préstamos y devoluciones mediante una interfaz web sencilla y funcional.

El sistema fue desarrollado con fines académicos para aplicar conceptos de desarrollo web utilizando el framework Django y bases de datos relacionales


Objetivos del proyecto

* Facilitar la administración de libros dentro de una biblioteca.
* Llevar control de préstamos y devoluciones.
* Gestionar usuarios del sistema.
* Aplicar conceptos de desarrollo web con Django.


Funcionalidades

* Registro de libros.
* Edición y eliminación de libros.
* Gestión de usuarios.
* Registro de préstamos.
* Registro de devoluciones.
* Panel de administración de Django.
* Interfaz web accesible desde navegador.

Tecnologías utilizadas

* Python 3
* Django
* HTML5
* CSS3
* Bootstrap
* SQLite


Requisitos

Antes de ejecutar el proyecto se debe tener instalado:

* Python 3
* pip
* Git
* Django

Verificar instalación:
python --version
pip --version
1. Clonar el repositorio:
git clone https://github.com/Carrasquilla24/sistema-biblioteca-django.git
2. Ingresar a la carpeta del proyecto:
cd sistema-biblioteca-django
3. Crear entorno virtual
Windows:
python -m venv env
env\Scripts\activate
4. Instalar dependencias:
pip install -r requirements.txt
Migraciones
Ejecutar las migraciones para crear la base de datos:
python manage.py migrate

Ejecución del servidor
Iniciar el servidor local:
python manage.py runserver


Base de datos

El sistema utiliza SQLite como gestor de base de datos por defecto, el cual se integra automáticamente con Django.

Autor

Proyecto desarrollado por Carrasquilla24 con fines académicos y educativos.

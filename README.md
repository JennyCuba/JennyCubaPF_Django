# Proyecto Final Django - Gestión de Artículos

Este proyecto es una aplicación web desarrollada con Django diseñada para el registro, búsqueda y control de artículos para la venta.

## Descripción

El sistema permite a los usuarios administrar un inventario de artículos, facilitando la gestión de productos disponibles para la venta. Proporciona funcionalidades para agregar nuevos artículos, ver un listado de los artículos existentes, buscar artículos específicos y controlar la información asociada a cada uno.

## Características

*   **Registro de Artículos:** Permite agregar nuevos artículos al sistema, incluyendo detalles como nombre, descripción, precio, etc.
*   **Listado de Artículos:** Muestra todos los artículos registrados en la base de datos.
*   **Búsqueda de Artículos:** Facilita la búsqueda de artículos específicos dentro del inventario.
*   **Control de Artículos:** Permite ver y gestionar la información detallada de cada artículo.

## Tecnologías Utilizadas

*   **Python:** Lenguaje de programación principal.
*   **Django:** Framework web de alto nivel para Python.
*   **HTML/CSS/JavaScript:** Para la interfaz de usuario.
*   **SQLite (por defecto en Django):** Base de datos para el almacenamiento de la información (puede ser configurada para usar otras bases de datos como PostgreSQL, MySQL, etc.).

## Setup y Instalación

Siga estos pasos para configurar y ejecutar el proyecto en su entorno local:

1.  **Clonar el repositorio (si aplica):**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd JennyCuba_ProyectoFinal_Django
    ```

2.  **Crear y activar un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    Asegúrese de tener un archivo `requirements.txt` con todas las dependencias del proyecto.
    ```bash
    pip install -r requirements.txt
    ```
    Si no tiene un archivo `requirements.txt`, puede generarlo con `pip freeze > requirements.txt` después de instalar Django y otras librerías necesarias. Como mínimo, necesitará Django:
    ```bash
    pip install Django
    ```

4.  **Aplicar las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario (opcional, para acceder al panel de administración de Django):**
    ```bash
    python manage.py createsuperuser
    ```
    Siga las instrucciones para ingresar nombre de usuario, correo electrónico y contraseña.

## Ejecutar la Aplicación

Una vez completada la instalación, puede ejecutar el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/` en su navegador web.

## Estructura del Proyecto (Resumen)

*   `manage.py`: Utilidad de línea de comandos para interactuar con el proyecto Django.
*   `JennyCubaPF_Django/`: Directorio principal del proyecto.
    *   `settings.py`: Configuración del proyecto.
    *   `urls.py`: Definiciones de URL a nivel de proyecto.
    *   `wsgi.py` / `asgi.py`: Puntos de entrada para servidores WSGI/ASGI.
*   `inicio/`: Aplicación Django para la gestión de artículos.
    *   `models.py`: Definición de los modelos de datos (tablas de la base de datos).
    *   `views.py`: Lógica de las vistas (controladores).
    *   `urls.py`: Definiciones de URL a nivel de aplicación.
    *   `forms.py`: Definición de formularios.
    *   `admin.py`: Configuración para el panel de administración de Django.
    *   `templates/`: Plantillas HTML para la interfaz de usuario.
    *   `static/`: Archivos estáticos (CSS, JavaScript, imágenes).
    *   `migrations/`: Archivos de migración de la base de datos.
*   `Templates/`: Directorio para plantillas base o globales.
*   `requirements.txt`: Lista de dependencias del proyecto.
*   `README.md`: Este archivo.

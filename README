# Asistente de Recetas

Este proyecto es un **Asistente de Recetas** que utiliza **FastAPI**, **Cohere** y una base de datos MySQL para generar y mostrar recetas basadas en las consultas del usuario. El asistente devuelve recetas con información nutricional y consejos detallados en español.

## Tabla de Contenido

- [Requisitos](#requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación y Configuración](#instalación-y-configuración)
- [Ejecución Local (sin Docker)](#ejecución-local-sin-docker)
- [Ejecución con Docker](#ejecución-con-docker)
- [Pruebas](#pruebas)
- [Uso](#uso)
- [Personalización](#personalización)
- [Contribuciones y Licencia](#contribuciones-y-licencia)

---

## Requisitos

1. **Python 3.9+** (la versión usada en el Dockerfile).  
2. **Docker** (opcional, si deseas ejecutar la aplicación en contenedores).  
3. **MySQL** (local o remoto) y credenciales de conexión.

---

## Estructura del Proyecto

```bash
.
├── api.py               
├── db.py                
├── requirements.txt     
├── Dockerfile           
├── templates/
│   └── index.html       
├── test.py              
├── .env.example         
└── ...
```

- api.py: Contiene la lógica principal de FastAPI, incluyendo endpoints /health y /chat, y la función de parseo de recetas.
- db.py: Se encarga de conectar a MySQL (usando variables de entorno).
- templates/index.html: Interfaz web para interactuar con el asistente.
test.py: Permite probar los endpoints con requests.
Dockerfile: Define la imagen Docker para desplegar la aplicación.
Instalación y Configuración

1. Clonar o descargar el repositorio
```bash

git clone https://github.com/tu-repositorio/asistente-recetas.git
cd asistente-recetas
```
2. Instalar dependencias
```bash
Copiar
pip install -r requirements.txt
```

3. Configurar variables de entorno
Copia el archivo .env.example y renómbralo a .env:

```bash

cp .env.example .env
```
Abre .env y completa tus credenciales:

```bash

DB_HOST=your-db-endpoint.rds.amazonaws.com
DB_PORT=3306
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
COHERE_API_KEY=your_cohere_key
```
Asegúrate de que tu base de datos MySQL exista y tengas acceso desde tu IP o contenedor.

## Ejecución Local (sin Docker)
 
Iniciar el servidor FastAPI con Uvicorn:

```bash

uvicorn api:app --reload
```
Verás algo como:

```bash
INFO:     Uvicorn running on http://127.0.0.1:8000
``` 
Abrir la aplicación en tu navegador en http://127.0.0.1:8000.

Verás la interfaz index.html con el formulario de búsqueda de recetas.
Consultar la salud de la app en http://127.0.0.1:8000/health.

## Ejecución con Docker
Construir la imagen:

```bash

docker build -t mi-asistente-recetas .
```
## Ejecutar el contenedor:

```bash
docker run -d -p 80:80 --name cont-asistente-recetas mi-asistente-recetas
Abre tu navegador en http://localhost (puerto 80) para ver la aplicación corriendo en Docker.
Asegúrate de pasar las variables de entorno necesarias o configurar tu .env dentro del contenedor (por ejemplo, con --env-file .env).
```
## Pruebas
El archivo test.py contiene pruebas sencillas para verificar:

/health devuelva {"status": "OK"}.
/chat acepte una pregunta y devuelva un JSON con la clave "recipes".
Cómo ejecutar las pruebas
Asegúrate de tener el servidor corriendo (por ejemplo, uvicorn api:app --reload).

En otra terminal, ejecuta:
```bash

python test.py
``` 
Verás en la consola:
```bash

Iniciando pruebas...
✓ /health funciona correctamente.
✓ /chat funciona correctamente y devuelve 'recipes'.
Todas las pruebas han finalizado con éxito.
```

## Uso
- Abre la app en tu navegador en http://127.0.0.1:8000 (o el puerto que uses).
- Ingresa en el campo de texto algo como “Recetas con bajo índice glucémico” y presiona Buscar.
- El servidor envía la consulta a Cohere y genera recetas en español, detallando ingredientes, tiempos de cocción, índice glucémico, etc.
- El resultado se muestra en tarjetas en la página, y la interacción se registra en la base de datos (tabla interactions).

## Personalización
- Prompt: Edita la variable system_prompt en api.py para ajustar el estilo o contenido de las recetas - generadas.
- Estilos: Modifica el archivo templates/index.html para cambiar la apariencia (usa Bootstrap, CSS personalizado, etc.).
- Base de datos: Cambia la lógica de db.py si deseas otra tabla o motor de base de datos.

## Contribuciones y Licencia
Siente libre de hacer pull requests o abrir issues para mejoras.

¡Listo! Con esto tienes todo lo necesario para ejecutar, probar y personalizar tu Asistente de Recetas con FastAPI y Cohere.
¡Disfruta y a cocinar!
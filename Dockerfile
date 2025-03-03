# Usa una imagen oficial de Python (versión 3.9, por ejemplo)
FROM python:3.11-slim

# Desactiva buffering para que los logs aparezcan en tiempo real
ENV PYTHONUNBUFFERED=1

# Crea un directorio de trabajo en el contenedor
WORKDIR /app

# Copia los requirements al contenedor
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo tu código al contenedor
COPY . .

# Expón el puerto 80 (o el que uses)
EXPOSE 8000

# Comando para lanzar la aplicación con Uvicorn en el puerto 80
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

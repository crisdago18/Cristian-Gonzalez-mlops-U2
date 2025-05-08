# Imagen base
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todos los archivos al contenedor
COPY . .

# Instalar las dependencias necesarias
RUN pip install -r requirements.txt

# Comando para correr la aplicación
CMD ["python", "app.py"]

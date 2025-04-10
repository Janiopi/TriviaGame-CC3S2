# Usa una imagen oficial de Python como base
FROM python:3.11-slim-bullseye

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt dentro del contenedor
COPY requirements.txt .

# Instala las dependencias dentro del contenedor
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Expone el puerto en el que FastAPI correrá
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

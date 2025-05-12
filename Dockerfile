# Imagen base de Python
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar el script y requirements.txt al contenedor
COPY fake_data.py .
COPY requirements.txt .

# Instalar dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto al iniciar el contenedor
CMD ["python", "fake_data.py"]
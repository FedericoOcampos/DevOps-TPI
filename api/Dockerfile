FROM python:3.10-slim

WORKDIR /app

# Copiar y instalar dependencias primero (mejor cache de layers)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY main.py .

# Render asigna el puerto automáticamente via $PORT
# No necesitas EXPOSE para Render, pero lo dejamos para claridad
EXPOSE $PORT

# Usar variables de entorno para el puerto
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
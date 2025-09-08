FROM python:3.10-slim

WORKDIR /app

# Copiar y instalar dependencias primero (mejor cache de layers)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY main.py .

# Render asigna el puerto automáticamente via $PORT
# Definimos un valor por defecto y exponemos el puerto de la app (8000)
ENV PORT=8000
EXPOSE 8000

# Usar variables de entorno para el puerto al iniciar uvicorn
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}" ]
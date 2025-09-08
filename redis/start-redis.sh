#!/bin/bash

if [ -z "$PORT" ]; then
    echo "PORT no definido, usando 6379 por defecto"
    PORT=6379
fi

echo "🚀 Iniciando Redis en puerto $PORT"

# Crear una configuración temporal con el puerto de Render
cp /usr/local/etc/redis/redis.conf /tmp/redis-render.conf

# Reemplazar el puerto en la configuración
if grep -q "^port[[:space:]]\+" /tmp/redis-render.conf; then
    sed -i "s/^port.*/port $PORT/" /tmp/redis-render.conf
else
    echo "port $PORT" >> /tmp/redis-render.conf
fi

echo "📋 Configuración de Redis:"
echo "Puerto: $PORT"
echo "Configuración aplicada:"
grep "^port\|^bind\|^save" /tmp/redis-render.conf

# Verificar que el directorio de datos existe
if [ ! -d "/data" ]; then
    mkdir -p /data
fi

# Iniciar Redis con la configuración modificada
echo "✅ Iniciando servidor Redis..."
exec redis-server /tmp/redis-render.conf
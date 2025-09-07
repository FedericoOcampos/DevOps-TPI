#!/bin/sh

echo "🚀 Iniciando servidor web en puerto $PORT"

# Reemplazar el placeholder del puerto en la configuración de nginx
sed -i "s/RENDER_PORT/$PORT/g" /etc/nginx/nginx.conf

# Mostrar la configuración final (para debug)
echo "📋 Configuración de nginx:"
cat /etc/nginx/nginx.conf

# Verificar la configuración de nginx
nginx -t

# Iniciar nginx en primer plano
echo "✅ Iniciando nginx..."
nginx -g 'daemon off;'
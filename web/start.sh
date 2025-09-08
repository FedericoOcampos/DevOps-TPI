#!/bin/sh

echo "🚀 Iniciando servidor web en puerto $PORT"

# Reemplazar el placeholder del puerto en la configuración de nginx
sed -i "s/RENDER_PORT/$PORT/g" /etc/nginx/nginx.conf

# Si se definió API_BASE, inyectarla como meta tag en index.html para que app.js la use
if [ -n "$API_BASE" ]; then
	echo "📡 Inyectando API_BASE=$API_BASE en index.html"
	# Insertar la meta tag justo antes de </head>
	sed -i "/<\/head>/i <meta name=\"api-base\" content=\"${API_BASE}\">" /usr/share/nginx/html/index.html || true
fi

# Mostrar la configuración final (para debug)
echo "📋 Configuración de nginx:"
cat /etc/nginx/nginx.conf

# Verificar la configuración de nginx
nginx -t

# Iniciar nginx en primer plano
echo "✅ Iniciando nginx..."
nginx -g 'daemon off;'
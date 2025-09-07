FROM nginx:alpine

# Copiar archivos estáticos
COPY index.html /usr/share/nginx/html/
COPY app.js /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/

# Copiar configuración personalizada de nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copiar script de inicio
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Render asigna el puerto automáticamente
EXPOSE $PORT

# Usar el script de inicio
CMD ["/start.sh"]
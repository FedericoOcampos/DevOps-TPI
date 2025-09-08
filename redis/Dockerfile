FROM redis:alpine

# Instalar herramientas básicas para debugging (opcional)
RUN apk add --no-cache bash

# Crear directorio para datos
RUN mkdir -p /data && chown redis:redis /data

# Copiar configuración personalizada
COPY redis.conf /usr/local/etc/redis/redis.conf

# Hacer el archivo de configuración legible
RUN chmod 644 /usr/local/etc/redis/redis.conf

# Exponer puerto (Render usará el que asigne)
## Exponer el puerto de Redis por claridad; Render puede mapear su propio puerto al contenedor
EXPOSE 6379

# Script para usar el puerto dinámico de Render
COPY start-redis.sh /start-redis.sh
RUN chmod +x /start-redis.sh

# Cambiar al usuario redis por seguridad
# No cambiar al usuario 'redis' aquí para que el script pueda crear /data si es necesario;
# Render corre contenedores en entornos aislados; revisa permisos en producción.

# Usar el script de inicio que manejará el puerto dinámico
CMD ["/start-redis.sh"]
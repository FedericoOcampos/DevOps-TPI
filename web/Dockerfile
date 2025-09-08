FROM nginx:alpine

# Remove default nginx content and copy app
RUN rm -rf /usr/share/nginx/html/*
COPY . /usr/share/nginx/html
# Copy the repository nginx config into the container nginx location so start.sh can
# replace the placeholder port (RENDER_PORT) with the runtime $PORT.
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the start script and make it executable
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Expose the port (Render provides $PORT at runtime)
EXPOSE ${PORT:-80}

# Run custom start script which will replace placeholders and start nginx
CMD ["/start.sh"]

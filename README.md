# Mi Aplicación Redis

Aplicación web con FastAPI, Redis y frontend estático.

## 🚀 Setup Local

### Prerrequisitos
- Docker y Docker Compose instalados
- Git

### Configuración inicial

1. **Clonar el repositorio:**
   ```bash
   git clone <tu-repo-url>
   cd tu-proyecto
   ```

2. **Configurar variables de entorno:**
   ```bash
   # Copiar el archivo de ejemplo
   cp .env.example .env
   
   # El archivo .env ya tiene los valores correctos para desarrollo local
   # No necesitas modificar nada para empezar
   ```

3. **Levantar los servicios:**
   ```bash
   docker-compose up -d
   ```

4. **Verificar que funciona:**
   - Frontend: http://localhost:8080
   - API: http://localhost:8000
   - API Health: http://localhost:8000/health

### Variables de entorno

| Variable | Descripción | Valor Local | Valor Producción |
|----------|-------------|-------------|------------------|
| `ENVIRONMENT` | Entorno actual | `local` | `production` |
| `REDIS_HOST` | Host de Redis | `redis` | Auto (Render) |
| `REDIS_PORT` | Puerto Redis | `6379` | Auto (Render) |
| `REDIS_URL` | URL completa | Auto generada | Auto (Render) |

### Estructura del proyecto

```
├── .env.example          # Plantilla de variables (SÍ en Git)
├── .env                  # Variables locales (NO en Git)
├── docker-compose.yml    # Configuración Docker local
├── render.yaml          # Configuración para producción
├── api/
│   ├── main.py          # API principal
│   ├── config.py        # Configuración por entornos
│   └── Dockerfile       # Imagen Docker de la API
└── web/
    ├── index.html       # Frontend
    ├── app.js          # Lógica del frontend
    └── style.css       # Estilos
```

## 🔧 Desarrollo

### Comandos útiles
```bash
# Ver logs de todos los servicios
docker-compose logs -f

# Ver logs solo de la API
docker-compose logs -f api

# Reiniciar un servicio específico
docker-compose restart api

# Parar todo
docker-compose down
```

### Agregar nuevas variables de entorno

1. Agregar la variable en `.env.example` con valor de ejemplo
2. Agregar en `api/config.py` en la clase `Settings`
3. Actualizar este README con la documentación
4. En producción (Render) se configura automáticamente via `render.yaml`

## 🚀 Deployment

El proyecto se despliega automáticamente en Render usando el archivo `render.yaml`.

### Servicios en producción:
- **Redis**: Servicio nativo de Render
- **API**: https://api-[hash].onrender.com  
- **Frontend**: https://web-[hash].onrender.com

## 🤝 Contribuir

1. Hacer fork del repositorio
2. Crear rama feature: `git checkout -b feature/nueva-funcionalidad`
3. Hacer commit: `git commit -am 'Agregar nueva funcionalidad'`
4. Push a la rama: `git push origin feature/nueva-funcionalidad`
5. Crear Pull Request

## 📞 Soporte

Si tienes problemas con el setup local:
1. Verifica que Docker esté corriendo
2. Revisa que el archivo `.env` existe y tiene los valores correctos
3. Verifica el endpoint `/health` de la API
4. Revisa los logs con `docker-compose logs -f`
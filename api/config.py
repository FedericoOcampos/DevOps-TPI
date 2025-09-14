# ===== api/config.py =====
import os
from typing import List

class Settings:
    def __init__(self):
        # === CONFIGURACIÓN BÁSICA ===
        self.environment: str = os.getenv('ENVIRONMENT', 'local')
        self.debug: bool = self.environment == 'local'
        
        # === CONFIGURACIÓN REDIS ===
        if self.environment == 'local':
            # Local: usando Docker Compose
            redis_host = os.getenv('REDIS_HOST', 'redis')
            redis_port = os.getenv('REDIS_PORT', '6379')
            self.redis_url = f"redis://{redis_host}:{redis_port}"
        else:
            # Producción: usando variable automática de Render
            self.redis_url = os.getenv('REDIS_URL', '')
            if not self.redis_url:
                raise ValueError("REDIS_URL no configurada en producción")
        
        # === CONFIGURACIÓN CORS ===
        self.cors_origins = self._get_cors_origins()
        
        # === CONFIGURACIÓN DEL SERVIDOR ===
        self.port = int(os.getenv('PORT', '8000'))
        self.host = '0.0.0.0'  # Para que funcione en contenedores
        
        # === URLs Y DOMINIOS ===
        self.service_name = os.getenv('RENDER_SERVICE_NAME', 'api')
        self.external_url = os.getenv('RENDER_EXTERNAL_URL', f'http://localhost:{self.port}')
        
    def _get_cors_origins(self) -> List[str]:
        """Configuración de CORS según el entorno"""
        if self.environment == 'local':
            return [
                "http://localhost:8080",
                "http://127.0.0.1:8080",
                "http://localhost:3000",
                "https://web-py62.onrender.com/",
            ]
        else:
            # En producción, Render puede pasar la URL del frontend como variable
            frontend_url = os.getenv('FRONTEND_URL', '')
            origins = []
            
            if frontend_url:
                origins.append(frontend_url)
            
            # También permitir el dominio base de tu proyecto
            origins.extend([
                "https://web-*.onrender.com",  # Patrón para servicios de Render
                # Agrega aquí dominios específicos si los conoces
            ])
            
            return origins
    
    def get_redis_client(self):
        """Factory para crear cliente Redis"""
        import redis
        try:
            return redis.from_url(self.redis_url, decode_responses=True)
        except Exception as e:
            raise ConnectionError(f"Error conectando a Redis: {e}")
    
    def is_production(self) -> bool:
        return self.environment == 'production'
    
    def is_local(self) -> bool:
        return self.environment == 'local'

# === INSTANCIA GLOBAL ===
settings = Settings()

# === FUNCIÓN DE UTILIDAD ===
def get_settings() -> Settings:
    """Obtiene la configuración global"""
    return settings
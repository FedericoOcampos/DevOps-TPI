import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import redis

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión a Redis usando variables de entorno
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
print(f"Conectando a Redis: {redis_url}")

try:
    # Usar from_url para mayor flexibilidad con URLs completas
    r = redis.from_url(redis_url, decode_responses=True)
    # Test de conexión
    r.ping()
    print("✅ Conexión a Redis exitosa")
except Exception as e:
    print(f"❌ Error conectando a Redis: {e}")
    r = None

@app.get("/")
def root():
    return {"message": "API funcionando", "redis_connected": r is not None}

@app.get("/health")
def health_check():
    if r is None:
        return {"status": "unhealthy", "redis": "disconnected"}
    
    try:
        r.ping()
        return {"status": "healthy", "redis": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "redis": f"error: {str(e)}"}

@app.get("/get/{key}")
def get_value(key: str):
    if r is None:
        raise HTTPException(status_code=500, detail="Redis no disponible")
    
    try:
        value = r.get(key)
        return {"key": key, "value": value}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error obteniendo valor: {str(e)}")

@app.post("/set/{key}/{value}")
def set_value(key: str, value: str):
    if r is None:
        raise HTTPException(status_code=500, detail="Redis no disponible")
    
    try:
        r.set(key, value)
        return {"message": f"Set {key} = {value}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error estableciendo valor: {str(e)}")
from fastapi import FastAPI
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

# Conexion a Redis (no hace falta utilizar puertos explicitamente)
# r = redis.Redis(host="redis", port=6379, decode_responses=True)
r = redis.Redis(host="redis", decode_responses=True)

@app.get("/get/{key}")
def get_value(key: str):
    value = r.get(key)
    return {"key": key, "value": value}

@app.post("/set/{key}/{value}")
def set_value(key: str, value: str):
    r.set(key, value)
    return {"message": f"Set {key} = {value}"}
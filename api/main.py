from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import redis
import json
import uuid

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# To do app api
class Task(BaseModel):
    id: str
    text: str
    completed: bool = False
    created_at: str = datetime.utcnow().isoformat()

@app.post("/tasks", response_model=Task)
def create_task(text: str):
    task_id = str(uuid.uuid4())
    task = Task(id=task_id, text=text, completed=False)
    r.hset("tasks", task_id, task.json())
    return task

@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # Obtenemos todas las tareas de Redis
    tasks = [Task(**json.loads(t)) for t in r.hvals("tasks")]
    
    # Ordenamos por created_at descendente
    tasks.sort(key=lambda t: datetime.fromisoformat(t.created_at), reverse=True)
    
    return tasks

@app.post("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: str):
    data = r.hget("tasks", task_id)
    print(f"data complete: {data}")
    if not data:
        raise HTTPException(404, "Task not found")
    task = Task(**json.loads(data))
    task.completed = True
    r.hset("tasks", task_id, task.json())
    return task

@app.post("/tasks/{task_id}/incomplete", response_model=Task)
def incomplete_task(task_id: str):
    data = r.hget("tasks", task_id)
    print(f"data complete: {data}")
    if not data:
        raise HTTPException(404, "Task not found")
    task = Task(**json.loads(data))
    task.completed = False
    r.hset("tasks", task_id, task.json())
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    if not r.hdel("tasks", task_id):
        raise HTTPException(404, "Task not found")
    return {"ok": True}
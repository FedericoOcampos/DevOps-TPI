const API = "http://localhost:8010";

async function fetchTasks() {
    const res = await fetch(`${API}/tasks`);
    const tasks = await res.json();
    const list = document.getElementById("taskList");
    list.innerHTML = "";
    tasks.forEach(task => {
    const li = document.createElement("li");
    li.className = "task-card";
    li.innerHTML = `
        <button class="task-btn" onclick="toggleTask('${task.id}', ${task.completed})">
        <i class="bi ${task.completed ? 'bi-check-circle-fill' : 'bi-circle'}"></i>
        </button>
        <span class="task-text ${task.completed ? 'done' : ''}">${task.text}</span>
        <button class="task-btn" onclick="deleteTask('${task.id}')">
        <i class="bi bi-x"></i>
        </button>
    `;
    list.appendChild(li);
    });
}

async function addTask() {
    const input = document.getElementById("taskInput");
    const text = input.value.trim();
    if (!text) return;
    await fetch(`${API}/tasks?text=${encodeURIComponent(text)}`, { method: "POST" });
    input.value = "";
    fetchTasks();
}

async function toggleTask(id, completed) {
    console.log("toggleTask:", id, completed);
    if (completed) {
    // desmarcar = volver a guardar como incompleta
    await fetch(`${API}/tasks/${id}/incomplete`, { method: "POST" });
    } else {
    // marcar como completa
    await fetch(`${API}/tasks/${id}/complete`, { method: "POST" });
    }
    fetchTasks();
}

async function deleteTask(id) {
    await fetch(`${API}/tasks/${id}`, { method: "DELETE" });
    fetchTasks();
}


fetchTasks();
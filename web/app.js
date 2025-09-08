// Configuración de la API - se adaptará automáticamente al entorno
const API_BASE_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:8000'  // Desarrollo local
    : 'https://tu-proyecto-api.onrender.com';  // Producción en Render

function openSetModal() {
    document.getElementById("setModal").style.display = "block";
}

function openGetModal() {
    document.getElementById("getModal").style.display = "block";
}

function closeModal(id) {
    document.getElementById(id).style.display = "none";
}

function showMessage(message) {
    const box = document.getElementById("messageBox");
    box.innerText = message;
    box.style.display = "block";
}

async function setValue() {
    const key = document.getElementById("setKey").value;
    const value = document.getElementById("setValue").value;

    if (!key || !value) {
        showMessage("Debes ingresar una clave y un valor.");
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/set/${key}/${value}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (response.ok) {
            showMessage("¡Clave guardada!");
            closeModal("setModal");
            // Limpiar campos
            document.getElementById("setKey").value = '';
            document.getElementById("setValue").value = '';
        } else {
            showMessage("Error al guardar la clave");
        }
    } catch (error) {
        console.error('Error:', error);
        showMessage("Error de conexión con el servidor");
    }
}

async function getValue() {
    const key = document.getElementById("getKey").value;

    if (!key) {
        showMessage("Debes ingresar una clave.");
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/get/${key}`);
        
        if (response.ok) {
            const data = await response.json();
            const value = data.value !== null ? data.value : "No encontrado";
            showMessage(`Valor para clave "${key}": ${value}`);
            closeModal("getModal");
            // Limpiar campo
            document.getElementById("getKey").value = '';
        } else {
            showMessage("Error al obtener el valor");
        }
    } catch (error) {
        console.error('Error:', error);
        showMessage("Error de conexión con el servidor");
    }
}

// Cerrar modal al hacer click fuera
window.onclick = function(event) {
    if (event.target.classList.contains("modal")) {
        event.target.style.display = "none";
    }
}

// Opcional: Mostrar en qué modo estamos
console.log('API URL:', API_BASE_URL);
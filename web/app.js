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

    await fetch(`http://localhost:8000/set/${key}/${value}`, {
        method: 'POST'
    });

    showMessage("¡Clave guardada!");
    closeModal("setModal");
}

async function getValue() {
    const key = document.getElementById("getKey").value;

    if (!key) {
        showMessage("Debes ingresar una clave.");
        return;
    }

    const response = await fetch(`http://localhost:8000/get/${key}`);
    const data = await response.json();
    const value = data.value !== null ? data.value : "No encontrado";

    showMessage(`Valor para clave "${key}": ${value}`);
    closeModal("getModal");
}

window.onclick = function(event) {
    if (event.target.classList.contains("modal")) {
        event.target.style.display = "none";
    }
}

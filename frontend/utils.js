function showError(id, message) {
    const el = document.getElementById(id);
    el.style.color = "red";
    el.innerText = message;
}

function showSuccess(id, message) {
    const el = document.getElementById(id);
    el.style.color = "green";
    el.innerText = message;
}

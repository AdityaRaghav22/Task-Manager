const API_BASE = "http://127.0.0.1:5000/api/v1";

// Save JWT
function saveToken(token) {
    localStorage.setItem("access_token", token);
}

// Get JWT
function getToken() {
    return localStorage.getItem("access_token");
}

// Auth fetch wrapper
async function authFetch(url, options = {}) {
    const token = getToken();

    options.headers = {
        ...(options.headers || {}),
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    };

    const res = await fetch(url, options);
    return res;
}

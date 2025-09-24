// Inicializar mapa en Rosario
var map = L.map('map').setView([-32.9587, -60.6939], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Cargar incidentes existentes
function cargarIncidentes() {
  fetch("/api/incidentes/")
    .then(res => res.json())
    .then(data => {
      data.forEach(inc => {
        if (inc.latitud && inc.longitud) {
          L.marker([inc.latitud, inc.longitud])
            .addTo(map)
            .bindPopup(`<b>${inc.titulo}</b><br>${inc.detalle}`);
        }
      });
    })
    .catch(err => console.error("Error cargando incidentes:", err));
}
cargarIncidentes();

// Click en mapa para crear incidente
map.on("click", function (e) {
  const token = localStorage.getItem("token");
  if (!token) {
    alert("Debes iniciar sesión para reportar un incidente.");
    return;
  }

  const titulo = prompt("Título del incidente:");
  const detalle = prompt("Detalle del incidente:");

  if (titulo && detalle) {
    fetch("/api/incidentes/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
      },
      body: JSON.stringify({
        titulo: titulo,
        detalle: detalle,
        latitud: e.latlng.lat,
        longitud: e.latlng.lng
      })
    })
      .then(res => {
        if (!res.ok) throw new Error("Error " + res.status);
        return res.json();
      })
      .then(data => {
        L.marker([data.latitud, data.longitud])
          .addTo(map)
          .bindPopup(`<b>${data.titulo}</b><br>${data.detalle}`);
        alert("Incidente reportado con éxito.");
      })
      .catch(err => alert("No se pudo guardar: " + err));
  }
});

// --- LOGIN ---
const btnLogin = document.getElementById("btnLogin");
const btnLogout = document.getElementById("btnLogout");
const btnRegister = document.getElementById("btnRegister");
const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");

btnLogin.onclick = () => { loginForm.classList.remove("hidden"); };
btnLogout.onclick = () => {
  localStorage.removeItem("token");
  btnLogout.classList.add("hidden");
  btnLogin.classList.remove("hidden");
  btnRegister.classList.remove("hidden");
  alert("Sesión cerrada");
};
document.getElementById("closeLogin").onclick = () => {
  loginForm.classList.add("hidden");
};
document.getElementById("doLogin").onclick = () => {
  const email = document.getElementById("emailLogin").value;
  const password = document.getElementById("passwordLogin").value;

  fetch("/api/token/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  })
    .then(async res => {
      if (!res.ok) {
        const errorData = await res.json();
        throw new Error("Login inválido: " + JSON.stringify(errorData));
      }
      return res.json();
    })
    .then(data => {
      localStorage.setItem("token", data.access);
      loginForm.classList.add("hidden");
      btnLogin.classList.add("hidden");
      btnRegister.classList.add("hidden");
      btnLogout.classList.remove("hidden");
      alert("Bienvenido!");
    })
    .catch(err => alert(err));
};

// --- REGISTRO ---
btnRegister.onclick = () => { registerForm.classList.remove("hidden"); };
document.getElementById("closeRegister").onclick = () => {
  registerForm.classList.add("hidden");
};
document.getElementById("doRegister").onclick = () => {
  const nombre = document.getElementById("nombre").value;
  const apellido = document.getElementById("apellido").value;
  const email = document.getElementById("emailRegister").value;
  const password = document.getElementById("passwordRegister").value;
  const rol = document.getElementById("rol").value;

  fetch("/api/usuarios/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre, apellido, email, password, rol })
  })
    .then(async res => {
      if (!res.ok) {
        const errorData = await res.json();
        throw new Error("Error en el registro: " + JSON.stringify(errorData));
      }
      return res.json();
    })
    .then(() => {
      registerForm.classList.add("hidden");
      alert("Usuario registrado. Ahora puedes iniciar sesión.");
    })
    .catch(err => alert(err));
};

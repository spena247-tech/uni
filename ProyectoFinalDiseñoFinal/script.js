const CONFIG = {
  universidadNombre: "Universidad Autónoma de Bucaramanga",
  dominioCorreo: "@unab.edu.co",
  logoUrl: "./assets/logo_unab_mineducacion.png",
  fondoUnabUrl: "./assets/fondo_unab.jpg",
  programasAcademicos: [
    "Ingeniería de Sistemas", "Ingeniería Industrial", "Administración de Empresas",
    "Contaduría Pública", "Derecho", "Medicina", "Psicología", "Arquitectura",
    "Comunicación Social", "Negocios Internacionales"
  ]
};

const STATE = {
  usuario: {
    nombre: 'Cielo Castellanos', codigo: 'U00182939',
    programa: 'Ingeniería de Sistemas', semestre: '6to',
    correo: 'cielo.castellanos', fotoPerfil: 'https://i.ibb.co/WpRvPY4F/Gemini-Generated-Image-utj8ntutj8ntutj8.png',
    hlCompletadas: 74, hlTotal: 120, hlPendientes: 46
  },
  lugarActual: null,
  diaHorarioSeleccionado: null,
  registros: [
    { tipo: 'ESTUDIO GRUPAL', nombre: 'Casona UNAB', lugarId: 1, fecha: formatDisplayDate(new Date()), fechaISO: toISODate(new Date()), hora: '14:00 - 16:00', estado: 'activo' },
    { tipo: 'ENTRENAMIENTO', nombre: 'Gimnasio CSU', lugarId: 9, fecha: formatDisplayDate(addDays(new Date(), 1)), fechaISO: toISODate(addDays(new Date(), 1)), hora: '08:00 - 10:00', estado: 'activo' },
    { tipo: 'ESTUDIO INDEPENDIENTE', nombre: 'Biblioteca Luis Carlos Galán', lugarId: 6, fecha: formatDisplayDate(addDays(new Date(), -3)), fechaISO: toISODate(addDays(new Date(), -3)), hora: '10:00 - 12:00', estado: 'completado' }
  ],
  historialHL: [
    { fecha: '15 Oct 2023', lugar: 'Biblioteca Luis Carlos Galán', actividad: 'Estudio Independiente', horas: 4 },
    { fecha: '10 Oct 2023', lugar: 'Auditorio Mayor Luis Carlos Gómez Albarracín', actividad: 'Conferencia Tecnológica', horas: 2 },
    { fecha: '28 Sep 2023', lugar: 'Coliseo CSU', actividad: 'Práctica Libre', horas: 3 },
    { fecha: '15 Sep 2023', lugar: 'El Bosque', actividad: 'Lectura al aire libre', horas: 5 }
  ],
  favoritos: [8, 2, 6],
  noticias: [
    { categoria: 'Evento Institucional', titulo: 'Feria de Organizaciones Estudiantiles 2024', desc: 'Descubre nuevas oportunidades para sumar horas libres participando en los...', tiempo: 'Hoy, 10:00 AM', img: 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=400&q=80' },
    { categoria: 'Académico', titulo: 'Nuevos Espacios de Estudio Habilitados', desc: 'Se han habilitado 5 nuevas salas de estudio colaborativo en el Edificio K...', tiempo: 'Ayer', img: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400&q=80' },
    { categoria: 'Servicios', titulo: 'Horario Extendido en Biblioteca', desc: 'Durante la semana de parciales, la biblioteca principal operará 24/7 para...', tiempo: 'Hace 2 días', img: 'https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=400&q=80' }
  ]
};

const LUGARES = [
  { id: 1, nombre: 'Casona UNAB', tipo: 'CULTURA', categoria: 'Cultura', disponible: true, capacidad: 150, ocupados: 45, horario: 'Lunes a Viernes, 7:00 AM - 6:00 PM', desc: 'Patrimonio histórico de la universidad, ideal para eventos académicos, exposiciones y espacios de estudio tranquilo con un toque colonial.', ubicacion: 'Edificio Casona', img: 'https://unab.edu.co/wp-content/uploads/2022/01/2.Fachada-2-Casona.jpg' },
  { id: 2, nombre: 'El Bosque', tipo: 'RELAJACIÓN', categoria: 'Relax', disponible: true, capacidad: 100, ocupados: 20, horario: 'Lunes a Sábado, 6:00 AM - 6:00 PM', desc: 'Conexión directa con la naturaleza. Un ambiente verde y fresco perfecto para relajarse, leer un libro o conversar con amigos al aire libre.', ubicacion: 'Campus Principal, Zona Norte', img: 'https://tse4.mm.bing.net/th/id/OIP.KRSK1ivlNdrr5uHiUh1nMwHaE7?rs=1&pid=ImgDetMain&o=7&rm=3' },
  { id: 3, nombre: 'Cafetería Central', tipo: 'ALIMENTACIÓN', categoria: 'Alimentación', disponible: false, capacidad: 200, ocupados: 200, horario: 'Lunes a Viernes, 7:00 AM - 7:00 PM | Sábados, 8:00 AM - 2:00 PM', desc: 'El punto de encuentro principal para disfrutar de menús variados, almuerzos caseros y snacks rápidos entre clases.', ubicacion: 'Edificio Central, Piso 1', img: 'https://tse2.mm.bing.net/th/id/OIP.lJvkveG2pViIqz1tEl4KWgHaE8?rs=1&pid=ImgDetMain&o=7&rm=3' },
  { id: 4, nombre: 'Plaza Central UNAB', tipo: 'SOCIAL', categoria: 'Social', disponible: true, capacidad: 500, ocupados: 120, horario: 'Lunes a Domingo, 6:00 AM - 9:00 PM', desc: 'El corazón del campus, punto central de tránsito y encuentro, ideal para interactuar, descansar un momento y sentir la vibra universitaria.', ubicacion: 'Centro del Campus', img: 'https://unab.edu.co/wp-content/uploads/2022/01/Fachada-Unab-vertical.jpg' },
  { id: 5, nombre: 'Auditorio Mayor Luis Carlos Gómez Albarracín', tipo: 'CULTURA', categoria: 'Eventos', disponible: true, capacidad: 450, ocupados: 0, horario: 'Lunes a Viernes, 8:00 AM - 6:00 PM', desc: 'Principal escenario de la universidad para conferencias magistrales, grados, eventos culturales y foros institucionales.', ubicacion: 'Edificio Principal, Piso 2', img: 'https://unab.edu.co/wp-content/uploads/2022/01/3.-Auditorio-Mayor-Carlos-Gomez-Ibarra.jpg' },
  { id: 6, nombre: 'Biblioteca Luis Carlos Galán', tipo: 'ESTUDIO', categoria: 'Estudio', disponible: true, capacidad: 300, ocupados: 85, horario: 'Lunes a Viernes, 6:00 AM - 10:00 PM | Sábados, 8:00 AM - 5:00 PM', desc: 'Centro del conocimiento con amplias salas de lectura, cubículos de trabajo colaborativo y acceso a colecciones físicas y digitales.', ubicacion: 'Edificio L, Todos los pisos', img: 'https://unab.edu.co/wp-content/uploads/2022/01/11.-Bliblioteca-Luis-Carlos-Galan-Sarmiento.jpg' },
  { id: 7, nombre: 'Auditorio Jesús Alberto Rey Nariño', tipo: 'ACADÉMICO', categoria: 'Académico', disponible: true, capacidad: 200, ocupados: 0, horario: 'Lunes a Viernes, 8:00 AM - 8:00 PM', desc: 'Un espacio acústicamente acondicionado para presentaciones, debates académicos y eventos formativos de alta calidad.', ubicacion: 'Edificio Principal, Piso 1', img: 'https://unab.edu.co/wp-content/uploads/2022/01/8.-Interior-Auditorio-Jesu%CC%81s-alberto-Rey-Marin%CC%83o.jpg' },
  { id: 8, nombre: 'Cafetería Banú', tipo: 'ALIMENTACIÓN', categoria: 'Colaborativo', disponible: true, capacidad: 120, ocupados: 40, horario: 'Lunes a Viernes, 7:00 AM - 8:00 PM', desc: 'Plazoleta moderna al aire libre, perfecta para disfrutar de comidas ligeras, café y realizar trabajos colaborativos rodeado de áreas verdes.', ubicacion: 'Edificio Banú', img: 'https://unab.edu.co/wp-content/uploads/2022/01/10.-Plazoleta-Banu.jpg' },
  { id: 9, nombre: 'Gimnasio CSU', tipo: 'DEPORTE', categoria: 'Deporte', disponible: true, capacidad: 80, ocupados: 35, horario: 'Lunes a Sábado, 5:00 AM - 10:00 PM', desc: 'Complejo deportivo altamente equipado para el acondicionamiento físico, entrenamiento cardiovascular y fortalecimiento muscular.', ubicacion: 'Edificio CSU, Piso 1', img: 'https://unab.edu.co/wp-content/uploads/2022/01/4.-Gimnasio.jpg' },
  { id: 10, nombre: 'Salón Aeróbicos CSU', tipo: 'DEPORTE', categoria: 'Clases', disponible: true, capacidad: 40, ocupados: 12, horario: 'Lunes a Viernes, 6:00 AM - 9:00 PM', desc: 'Espacio diseñado para clases grupales, danza, yoga y entrenamiento funcional con acompañamiento guiado.', ubicacion: 'Edificio CSU, Piso 2', img: 'https://unab.edu.co/wp-content/uploads/2022/01/5.-Salon-de-aerobicos.jpg' },
  { id: 11, nombre: 'Coliseo CSU', tipo: 'DEPORTE', categoria: 'Deporte', disponible: false, capacidad: 200, ocupados: 200, horario: 'Lunes a Domingo, 6:00 AM - 10:00 PM', desc: 'Cancha múltiple techada para la práctica de baloncesto, voleibol, microfútbol y torneos deportivos interfacultades.', ubicacion: 'Edificio CSU', img: 'https://unab.edu.co/wp-content/uploads/2022/01/csu-4.jpg' }
];

const SVG = {
  home: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
  clock: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
  pin: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
  heart: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
  user: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
  search: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
  calendar: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
  check: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
  arrowRight: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
  x: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>',
  chair: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16M4 12h16M8 4v8M16 4v8M6 20v-4h12v4"/></svg>',
  heartFilled: '<svg viewBox="0 0 24 24" fill="#ef4444" stroke="#ef4444" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
  star: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
  calendarX: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/><line x1="10" y1="14" x2="14" y2="18"/><line x1="14" y1="14" x2="10" y2="18"/></svg>'
};

let filtroCategoria = 'Todos';
let busqueda = '';
let vistaActual = 'vista-login';
let historialVistas = [];
let fotoPerfilTemporal = '';

function addDays(date, days) {
  const next = new Date(date);
  next.setDate(next.getDate() + days);
  return next;
}

function toISODate(date) {
  const y = date.getFullYear();
  const m = String(date.getMonth() + 1).padStart(2, '0');
  const d = String(date.getDate()).padStart(2, '0');
  return `${y}-${m}-${d}`;
}

function formatDisplayDate(date) {
  return date.toLocaleDateString('es-ES', { day: 'numeric', month: 'short', year: 'numeric' }).replace(/ /g, ' ');
}

function logoMarkup(targetVista) {
  return `
    <a class="logo logo-unab" onclick="showVista('${targetVista}')">
      <img class="logo-img" src="${CONFIG.logoUrl}" alt="EntreHoras" />
      <span class="logo-text">EntreHoras</span>
    </a>`;
}

function avatarMarkup(sizeClass = '') {
  const cls = sizeClass ? ` ${sizeClass}` : '';
  if (STATE.usuario.fotoPerfil) {
    return `<img class="avatar-img${cls}" src="${STATE.usuario.fotoPerfil}" alt="Foto de ${STATE.usuario.nombre}" />`;
  }
  return `<span class="avatar-placeholder${cls}" aria-hidden="true">${SVG.user}</span>`;
}

function getLugarByRegistro(registro) {
  if (registro.lugarId) return LUGARES.find(l => l.id === registro.lugarId) || null;
  const nombre = registro.nombre.toLowerCase();
  return LUGARES.find(l => nombre.includes(l.nombre.toLowerCase()) || l.nombre.toLowerCase().includes(nombre)) || null;
}

function isFavorito(lugarId) {
  return STATE.favoritos.includes(lugarId);
}

function renderFavoriteButton(lugarId) {
  const activo = isFavorito(lugarId);
  return `<button class="btn-favorito${activo ? ' activo' : ''}" onclick="event.stopPropagation();toggleFavorito(${lugarId})" aria-label="${activo ? 'Quitar de favoritos' : 'Agregar a favoritos'}">
    ${activo ? SVG.heartFilled : SVG.heart}
  </button>`;
}

function getVistaActiva() {
  const activa = document.querySelector('.vista.activa');
  return activa ? activa.id : vistaActual;
}

/* ═══════════════════════════════════════════
   NAVEGACIÓN
═══════════════════════════════════════════ */
function showVista(id, guardarHistorial = true) {
  const previa = getVistaActiva();
  if (guardarHistorial && previa && previa !== id) {
    historialVistas.push(previa);
    if (historialVistas.length > 8) historialVistas.shift();
  }
  document.querySelectorAll('.vista').forEach(v => v.classList.remove('activa'));
  const target = document.getElementById(id);
  if (target) target.classList.add('activa');
  document.body.classList.toggle('dashboard-mode', isDashboardVista(id));
  document.body.classList.toggle('auth-mode', !isDashboardVista(id));
  vistaActual = id;
  window.scrollTo({ top: 0, behavior: 'smooth' });

  if (isDashboardVista(id)) {
    setHeaderDashboard();
  } else {
    setHeaderDefault();
  }
  setNavActivo(id);

  if (id === 'vista-dashboard') renderDashboard();
  if (id === 'vista-lugares') renderLugares();
  if (id === 'vista-detalle-lugar') renderDetalleLugar();
  if (id === 'vista-registro-exitoso') renderRegistroExitoso();
  if (id === 'vista-mis-hl') renderMisHL();
  if (id === 'vista-favoritos') renderFavoritos();
  if (id === 'vista-perfil') renderPerfil();
  if (id === 'vista-horario') renderHorario();
}

function volverVista(fallback = 'vista-dashboard') {
  const anterior = historialVistas.pop() || fallback;
  showVista(anterior, false);
}

function isDashboardVista(id) {
  return ['vista-dashboard', 'vista-mis-hl', 'vista-lugares', 'vista-detalle-lugar', 'vista-registro-exitoso', 'vista-favoritos', 'vista-perfil', 'vista-horario'].includes(id);
}

function setHeaderDefault() {
  const header = document.querySelector('.site-header');
  if (!header) return;
  header.innerHTML = logoMarkup('vista-login');
}

function setHeaderDashboard() {
  const header = document.querySelector('.site-header');
  if (!header) return;
  header.innerHTML = `
    ${logoMarkup('vista-dashboard')}
    <div class="header-actions">
      <div class="header-avatar" onclick="showVista('vista-perfil')" title="Ver perfil">
        ${avatarMarkup('avatar-sm')}
      </div>
      <button class="btn-logout-header" onclick="logout()">Salir</button>
    </div>`;
  updateUserLabels();
}

function setNavActivo(vistaId) {
  const labelMap = {
    'vista-dashboard': 'Inicio',
    'vista-mis-hl': 'Mis HL',
    'vista-lugares': 'Lugares',
    'vista-detalle-lugar': 'Lugares',
    'vista-registro-exitoso': 'Mis HL',
    'vista-favoritos': 'Favoritos',
    'vista-perfil': 'Perfil',
    'vista-horario': 'Horario'
  };
  const label = labelMap[vistaId];
  document.querySelectorAll('.sidebar-nav .nav-item').forEach(el => {
    el.classList.toggle('activo', Boolean(label && el.textContent.trim().includes(label)));
    if (el.classList.contains('activo')) el.setAttribute('aria-current', 'page');
    else el.removeAttribute('aria-current');
  });
  document.querySelectorAll('.bottom-nav .bottom-nav-item').forEach(el => {
    el.classList.toggle('activo', Boolean(label && el.textContent.trim().includes(label)));
    if (el.classList.contains('activo')) el.setAttribute('aria-current', 'page');
    else el.removeAttribute('aria-current');
  });
}

function updateUserLabels() {
  const u = STATE.usuario;
  document.querySelectorAll('.sidebar-nombre').forEach(el => { el.textContent = u.nombre; });
  document.querySelectorAll('.sidebar-avatar').forEach(el => { el.innerHTML = avatarMarkup('avatar-lg'); });
  document.querySelectorAll('.header-avatar').forEach(el => { el.innerHTML = avatarMarkup('avatar-sm'); });
}

/* ═══════════════════════════════════════════
   TOAST / HELPERS
═══════════════════════════════════════════ */
function setError(wrapId, errId, show) {
  const wrap = document.getElementById(wrapId);
  const err  = document.getElementById(errId);
  if (!wrap || !err) return;
  wrap.classList.toggle('error-field', show);
  err.classList.toggle('visible', show);
}

function clearErrors(ids) {
  ids.forEach(([w, e]) => setError(w, e, false));
}

function showToast(msg, tipo = 'exito') {
  const t = document.getElementById('toast');
  const icon = tipo === 'exito' ? '\u2705' : '\u26A0\uFE0F';
  t.textContent = `${icon}  ${msg}`;
  t.className = `toast ${tipo} show`;
  setTimeout(() => t.classList.remove('show'), 3500);
}

function togglePw(inputId, btn) {
  const input = document.getElementById(inputId);
  const isHidden = input.type === 'password';
  input.type = isHidden ? 'text' : 'password';
  btn.querySelector('svg').style.opacity = isHidden ? '.4' : '1';
  btn.setAttribute('aria-label', isHidden ? 'Ocultar contraseña' : 'Ver contraseña');
}

/* ═══════════════════════════════════════════
   REGISTRO
═══════════════════════════════════════════ */
function handleRegistro() {
  const nombre = document.getElementById('nombre').value.trim();
  const codigo = document.getElementById('codigo').value.trim().toUpperCase();
  const correo = document.getElementById('correo').value.trim();
  const programa = document.getElementById('programa').value;
  const semestre = document.getElementById('semestre').value;
  const pw = document.getElementById('password').value;
  const pw2 = document.getElementById('password2').value;
  const fields = [['wrap-nombre','err-nombre'],['wrap-codigo','err-codigo'],['wrap-correo','err-correo'],['wrap-programa','err-programa'],['wrap-semestre','err-semestre'],['wrap-password','err-password'],['wrap-password2','err-password2']];
  clearErrors(fields);
  let ok = true;
  const codigoReg = /^U\d{8}$/;
  if (!nombre) { setError('wrap-nombre','err-nombre',true); ok = false; }
  if (!codigoReg.test(codigo)) { setError('wrap-codigo','err-codigo',true); ok = false; }
  if (!correo) { setError('wrap-correo','err-correo',true); ok = false; }
  if (!programa) { setError('wrap-programa','err-programa',true); ok = false; }
  if (!semestre) { setError('wrap-semestre','err-semestre',true); ok = false; }
  if (pw.length < 8) { setError('wrap-password','err-password',true); ok = false; }
  if (pw !== pw2) { setError('wrap-password2','err-password2',true); ok = false; }
  if (!ok) { showToast('Revisa los campos marcados en rojo.', 'fallo'); return; }
  STATE.usuario.nombre = nombre;
  STATE.usuario.codigo = codigo;
  STATE.usuario.correo = correo;
  STATE.usuario.programa = programa;
  STATE.usuario.semestre = semestre;
  showToast('Cuenta creada para ' + nombre + ' \uD83C\uDF89', 'exito');
  setTimeout(() => { initDashboard(); showVista('vista-dashboard'); }, 1800);
}

/* ═══════════════════════════════════════════
   LOGIN
═══════════════════════════════════════════ */
function handleLogin() {
  const correo = document.getElementById('l-correo').value.trim();
  const pw = document.getElementById('l-password').value;
  clearErrors([['wrap-l-correo','err-l-correo'],['wrap-l-password','err-l-password']]);
  let ok = true;
  if (!correo) { setError('wrap-l-correo','err-l-correo',true); ok = false; }
  if (!pw) { setError('wrap-l-password','err-l-password',true); ok = false; }
  if (!ok) { showToast('Completa todos los campos.', 'fallo'); return; }
  showToast('\u00A1Bienvenido, ' + correo + '!', 'exito');
  setTimeout(() => { initDashboard(); showVista('vista-dashboard'); }, 1800);
}

function initDashboard() {
  setHeaderDashboard();
  bindStaticControls();
  updateUserLabels();
}

function logout() {
  cerrarModal();
  cerrarPerfilModal();
  showToast('Sesión cerrada.', 'exito');
  setTimeout(() => showVista('vista-login'), 350);
}

function bindStaticControls() {
  document.querySelectorAll('.btn-ver-horario').forEach(btn => {
    btn.setAttribute('type', 'button');
    btn.onclick = () => showVista('vista-horario');
  });
}

document.querySelectorAll('.input-wrap input, .input-wrap select').forEach(el => {
  el.addEventListener('input', () => {
    const wrap = el.closest('.input-wrap');
    if (wrap) {
      wrap.classList.remove('error-field');
      const errEl = wrap.parentElement.querySelector('.field-error');
      if (errEl) errEl.classList.remove('visible');
    }
  });
});

/* ═══════════════════════════════════════════
   RENDER — DASHBOARD
═══════════════════════════════════════════ */
function renderDashboard() {
  const container = document.getElementById('dash-content-inicio');
  if (!container) return;
  const u = STATE.usuario;
  const pendientes = u.hlTotal - u.hlCompletadas;
  const pct = Math.round((u.hlCompletadas / u.hlTotal) * 100);
  const circumference = 326.7;
  const offset = circumference * (1 - u.hlCompletadas / u.hlTotal);

  const noticiasHTML = STATE.noticias.map(n => {
    const badgeClass = n.categoria.includes('Evento') ? 'evento' : n.categoria.includes('Acad') ? 'academico' : 'servicio';
    return `<div class="noticia-card">
      <img class="noticia-img" src="${n.img}" alt="${n.titulo}" loading="lazy" />
      <div class="noticia-body">
        <span class="badge-cat ${badgeClass}">${n.categoria}</span>
        <h4 class="noticia-titulo">${n.titulo}</h4>
        <p class="noticia-desc">${n.desc}</p>
        <span class="noticia-tiempo">${n.tiempo}</span>
      </div>
    </div>`;
  }).join('');

  container.innerHTML = `
    <h1 style="font-size:1.8rem;font-weight:700;color:var(--color-acento);margin-bottom:4px;">Hola, ${u.nombre}</h1>
    <p style="color:var(--color-sublabel);margin-bottom:28px;">Bienvenido a tu panel de control acad\u00E9mico.</p>

    <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:24px;margin-bottom:32px;">
      <div class="card-stat">
        <h3 style="font-size:1.1rem;font-weight:700;color:var(--color-acento);margin-bottom:2px;">Resumen de Horas Libres</h3>
        <p style="font-size:.85rem;color:var(--color-sublabel);margin-bottom:16px;">Progreso actual de tu requisito institucional.</p>
        <div style="display:flex;flex-direction:column;align-items:center;gap:16px;">
          <svg width="120" height="120" viewBox="0 0 120 120">
            <circle cx="60" cy="60" r="52" fill="none" stroke="#e2e8f0" stroke-width="10"/>
            <circle cx="60" cy="60" r="52" fill="none" stroke="#f59e0b" stroke-width="10" stroke-dasharray="${circumference}" stroke-dashoffset="${offset}" stroke-linecap="round" transform="rotate(-90 60 60)"/>
            <text x="60" y="55" text-anchor="middle" font-size="24" font-weight="700" fill="#1e293b">${u.hlCompletadas}</text>
            <text x="60" y="72" text-anchor="middle" font-size="11" fill="#64748b">DE ${u.hlTotal} HRS</text>
          </svg>
          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <span style="display:inline-flex;padding:4px 12px;border-radius:20px;background:rgba(245,158,11,.12);color:var(--color-boton);font-size:.78rem;font-weight:600;">${u.hlCompletadas} Completadas</span>
            <span style="display:inline-flex;padding:4px 12px;border-radius:20px;background:rgba(100,116,139,.12);color:var(--color-sublabel);font-size:.78rem;font-weight:600;">${pendientes} Pendientes</span>
          </div>
        </div>
        <div style="margin-top:16px;padding:12px 16px;background:rgba(14,165,200,.08);border-radius:6px;font-size:.85rem;color:var(--color-acento);font-weight:500;">
          Te faltan ${pendientes} horas libres para completar tu requisito.
        </div>
      </div>

      <div>
        <h3 style="font-size:.85rem;font-weight:700;text-transform:uppercase;letter-spacing:.7px;color:var(--color-sublabel);margin-bottom:12px;">ACCESO R\u00C1PIDO</h3>
        <div class="acceso-rapido-item" onclick="showVista('vista-mis-hl')">
          <div class="acceso-rapido-icon">${SVG.pin}</div>
          <span class="acceso-rapido-texto">Mis lugares</span>
          <span style="color:var(--color-sublabel);">${SVG.arrowRight}</span>
        </div>
        <div class="acceso-rapido-item" onclick="showVista('vista-lugares')">
          <div class="acceso-rapido-icon">${SVG.chair}</div>
          <span class="acceso-rapido-texto">Lugares disponibles</span>
          <span style="color:var(--color-sublabel);">${SVG.arrowRight}</span>
        </div>
        <div class="acceso-rapido-item" onclick="showVista('vista-perfil')">
          <div class="acceso-rapido-icon">${SVG.user}</div>
          <span class="acceso-rapido-texto">Mi perfil</span>
          <span style="color:var(--color-sublabel);">${SVG.arrowRight}</span>
        </div>
      </div>
    </div>

    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
      <h2 style="font-size:1.3rem;font-weight:700;color:var(--color-acento);">Noticias del Campus</h2>
      <button class="btn-link-inline" onclick="showToast('Estas son todas las noticias disponibles por ahora.', 'exito')">Ver todas \u2192</button>
    </div>
    <div class="noticias-grid">${noticiasHTML}</div>`;
}

/* ═══════════════════════════════════════════
   RENDER — LUGARES
═══════════════════════════════════════════ */
function filtrarLugares() {
  return LUGARES.filter(l => {
    const matchCategoria = filtroCategoria === 'Todos' || l.categoria === filtroCategoria;
    const matchBusqueda = l.nombre.toLowerCase().includes(busqueda.toLowerCase()) || l.categoria.toLowerCase().includes(busqueda.toLowerCase());
    return matchCategoria && matchBusqueda;
  });
}

function setFiltro(cat) {
  filtroCategoria = cat;
  document.querySelectorAll('.filtro-btn').forEach(b => b.classList.toggle('activo', b.dataset.cat === cat));
  renderLugares();
}

function renderLugares() {
  const container = document.getElementById('dash-content-lugares');
  if (!container) return;
  const filtrados = filtrarLugares();
  const categorias = ['Todos', 'Deporte', 'Alimentaci\u00F3n', 'Estudio', 'Cultura', 'Salud'];

  container.innerHTML = `
    <h1 style="font-size:1.8rem;font-weight:700;color:var(--color-acento);margin-bottom:4px;">\u00BFD\u00F3nde puedo obtener mis HL?</h1>
    <p style="color:var(--color-sublabel);margin-bottom:16px;">Explora los diferentes espacios del campus...</p>
    <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;margin-bottom:8px;">
      <div class="search-bar">
        <span>${SVG.search}</span>
        <input type="text" id="busqueda-lugar" placeholder="Buscar lugar..." oninput="busqueda=this.value;renderLugares();" />
      </div>
    </div>
    <div class="filtros-wrap">
      ${categorias.map(c => `<button class="filtro-btn${c === filtroCategoria ? ' activo' : ''}" data-cat="${c}" onclick="setFiltro('${c}')">${c}</button>`).join('')}
    </div>
    <div class="lugares-grid">
      ${filtrados.length === 0 ? '<p style="color:var(--color-sublabel);grid-column:1/-1;text-align:center;padding:40px;">No se encontraron lugares.</p>' :
        filtrados.map(l => `
        <div class="lugar-card">
          <div class="lugar-img-wrap">
            <img class="lugar-img" src="${l.img}" alt="${l.nombre}" loading="lazy" />
            ${renderFavoriteButton(l.id)}
            <span class="badge-disp ${l.disponible ? 'disponible' : 'lleno'} lugar-badge-disp">${l.disponible ? '\u25CF Disponible' : '\u25CF Lleno'}</span>
          </div>
          <div class="lugar-body">
            <span class="lugar-tipo">${l.tipo}</span>
            <h3 class="lugar-nombre">${l.nombre}</h3>
            <p class="lugar-desc">${l.desc}</p>
            <button class="btn-lugar ${l.disponible ? 'disponible' : 'lleno'}"
              onclick="${l.disponible ? `verDetalleLugar(${l.id})` : ''}">
              ${l.disponible ? 'Registrarme \u2192' : 'Capacidad M\u00E1xima'}
            </button>
          </div>
        </div>`).join('')}
    </div>`;
}

function verDetalleLugar(id) {
  const lugar = LUGARES.find(l => l.id === id);
  if (!lugar) return;
  STATE.lugarActual = lugar;
  showVista('vista-detalle-lugar');
}

/* ═══════════════════════════════════════════
   RENDER — DETALLE LUGAR
═══════════════════════════════════════════ */
function renderDetalleLugar() {
  const container = document.getElementById('detalle-contenido');
  if (!container || !STATE.lugarActual) return;
  const l = STATE.lugarActual;
  container.innerHTML = `
    <div class="lugar-hero">
      <img src="${l.img}" alt="${l.nombre}" />
      ${renderFavoriteButton(l.id)}
      <div class="lugar-hero-overlay">
        <span class="lugar-hero-nombre">${l.nombre}</span>
        <span class="lugar-hero-subtipo">${l.tipo}</span>
      </div>
    </div>
    <div class="detalle-grid">
      <div>
        <h2 style="font-size:1.3rem;font-weight:700;color:var(--color-acento);margin-bottom:12px;">Sobre este lugar</h2>
        <p style="color:var(--color-texto);line-height:1.7;margin-bottom:16px;">${l.desc}</p>
        <div style="padding:16px;background:var(--color-fondo);border-radius:6px;">
          <p style="font-size:.82rem;color:var(--color-sublabel);">
            <strong>Normas del lugar:</strong> Mantener el orden, hacer silencio en zonas de estudio, y respetar los horarios establecidos. El uso de los espacios es exclusivo para estudiantes UNAB.
          </p>
        </div>
      </div>
      <div class="detalle-sidebar-card">
        <div class="detalle-info-row">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/></svg>
          <div><div class="detalle-info-label">Ubicaci\u00F3n</div><div class="detalle-info-valor">${l.ubicacion}</div></div>
        </div>
        <div class="detalle-info-row">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          <div><div class="detalle-info-label">Horario de operaci\u00F3n</div><div class="detalle-info-valor">${l.horario}</div></div>
        </div>
        <div class="detalle-info-row">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          <div><div class="detalle-info-label">Capacidad m\u00E1xima</div><div class="detalle-info-valor">${l.capacidad} personas (${l.ocupados} ocupados)</div></div>
        </div>
        <span class="badge-disp ${l.disponible ? 'disponible' : 'lleno'}" style="margin:8px 0 16px;justify-content:center;">${l.disponible ? '\u25CF Disponible para registro' : '\u25CF Lleno'}</span>
        <button class="btn-outline btn-fav-detalle" onclick="toggleFavorito(${l.id})">${isFavorito(l.id) ? 'Quitar de favoritos' : 'Agregar a favoritos'}</button>
        ${l.disponible ? `<button class="btn-primary" onclick="abrirModal()" style="margin-top:0;box-shadow:none;">Registrarme en este lugar</button>` :
          `<button class="btn-lugar lleno" style="margin-top:0;">Capacidad M\u00E1xima</button>`}
        <div class="nota-info">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          <span>Recuerda que el registro es v\u00E1lido por bloques de 2 horas continuas.</span>
        </div>
      </div>
    </div>`;
}

/* ═══════════════════════════════════════════
   MODAL
═══════════════════════════════════════════ */
function abrirModal() {
  const modal = document.getElementById('modal-confirmar');
  const text = document.getElementById('modal-text');
  if (text && STATE.lugarActual) {
    text.textContent = `\u00BFConfirmas tu registro en ${STATE.lugarActual.nombre}? Se asignar\u00E1 tu espacio seg\u00FAn la disponibilidad actual.`;
  }
  modal.classList.add('visible');
  document.body.style.overflow = 'hidden';
}

function cerrarModal() {
  document.getElementById('modal-confirmar').classList.remove('visible');
  document.body.style.overflow = '';
}

function confirmarRegistro() {
  cerrarModal();
  if (STATE.lugarActual) {
    const ahora = new Date();
    STATE.registros.unshift({
      tipo: STATE.lugarActual.tipo,
      nombre: STATE.lugarActual.nombre,
      lugarId: STATE.lugarActual.id,
      fecha: formatDisplayDate(ahora),
      fechaISO: toISODate(ahora),
      hora: 'Pr\u00F3ximas 2 horas',
      estado: 'activo'
    });
    STATE.diaHorarioSeleccionado = toISODate(ahora);
  }
  showVista('vista-registro-exitoso');
}

/* ═══════════════════════════════════════════
   RENDER — REGISTRO EXITOSO
═══════════════════════════════════════════ */
function renderRegistroExitoso() {
  const container = document.getElementById('dash-content-exitoso');
  if (!container || !STATE.lugarActual) return;
  const l = STATE.lugarActual;
  container.innerHTML = `
    <div class="exito-banner">
      <span style="width:28px;height:28px;border-radius:50%;background:var(--color-exito);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:16px;flex-shrink:0;">${SVG.check.replace('stroke-width="2"','stroke-width="3" width="16" height="16"')}</span>
      <div>
        <h3>\u00A1Registro Exitoso!</h3>
        <p>Tu espacio en ${l.nombre} ha sido reservado y confirmado.</p>
      </div>
    </div>
    <div class="lugar-hero" style="height:280px;margin-bottom:24px;">
      <img src="${l.img}" alt="${l.nombre}" />
      <div class="lugar-hero-overlay">
        <span style="font-size:1.4rem;font-weight:700;color:#fff;">${l.nombre}</span>
        <span style="font-size:.85rem;color:rgba(255,255,255,.75);">${l.tipo}</span>
      </div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 300px;gap:24px;">
      <div>
        <div class="info-cards-row">
          <div class="info-card-item">
            <div class="info-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/></svg></div>
            <div class="info-card-label">Ubicaci\u00F3n</div>
            <div class="info-card-val">${l.ubicacion}</div>
          </div>
          <div class="info-card-item">
            <div class="info-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
            <div class="info-card-label">Horario</div>
            <div class="info-card-val">${l.horario}</div>
          </div>
          <div class="info-card-item">
            <div class="info-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
            <div class="info-card-label">Capacidad</div>
            <div class="info-card-val">${l.capacidad} personas</div>
          </div>
        </div>
      </div>
      <div class="mi-registro-card">
        <div class="mi-registro-titulo">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          Mi Registro
        </div>
        <div class="mi-registro-label">Estado</div>
        <div class="mi-registro-valor" style="color:var(--color-exito);">\u25CF Activo</div>
        <div class="mi-registro-label">Bloque reservado</div>
        <div class="mi-registro-valor">Pr\u00F3ximas 2 horas</div>
        <button class="btn-primary" onclick="showVista('vista-mis-hl')" style="margin-top:0;box-shadow:none;">Ver mis registros</button>
        <button class="btn-link-cyan" onclick="showVista('vista-lugares')">Volver a Lugares</button>
      </div>
    </div>`;
}

/* ═══════════════════════════════════════════
   RENDER — MIS HL
═══════════════════════════════════════════ */
function switchTab(tab) {
  const activos = document.getElementById('tab-activos');
  const historial = document.getElementById('tab-historial');
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('activo'));
  document.getElementById('tab-btn-' + tab).classList.add('activo');
  if (activos) activos.style.display = tab === 'activos' ? 'grid' : 'none';
  if (historial) historial.style.display = tab === 'historial' ? 'block' : 'none';
}

function cancelarRegistro(idx) {
  STATE.registros.splice(idx, 1);
  renderMisHL();
  showToast('Registro cancelado.', 'exito');
}

function renderRegistroCard(registro, idx, puedeCancelar) {
  const lugar = getLugarByRegistro(registro);
  const img = lugar ? lugar.img : CONFIG.fondoUnabUrl;
  const estadoClass = registro.estado === 'activo' ? 'disponible' : '';
  const estadoTexto = registro.estado.charAt(0).toUpperCase() + registro.estado.slice(1);
  return `<article class="registro-card registro-card-visual registro-card-compacta">
    <img class="registro-thumb" src="${img}" alt="${registro.nombre}" loading="lazy" />
    <div class="registro-body">
      <span class="reg-tipo">${registro.tipo}</span>
      <h3 class="reg-nombre">${registro.nombre}</h3>
      <div class="reg-fecha">${SVG.calendar} ${registro.fecha} \u2022 ${registro.hora}</div>
      <span class="badge-disp ${estadoClass}" style="margin-top:12px;display:inline-flex;">\u25CF ${estadoTexto}</span>
    </div>
    ${puedeCancelar ? `<button class="btn-cancelar-reg" onclick="cancelarRegistro(${idx})" aria-label="Cancelar registro">${SVG.x}</button>` : ''}
  </article>`;
}

function renderMisHL() {
  const container = document.getElementById('dash-content-mis-hl');
  if (!container) return;
  const activos = STATE.registros.map((r, idx) => ({ ...r, idx })).filter(r => r.estado === 'activo');
  const completados = STATE.registros.map((r, idx) => ({ ...r, idx })).filter(r => r.estado === 'completado');

  let activosHTML;
  if (activos.length === 0) {
    activosHTML = `<div class="estado-vacio">
      <div class="estado-vacio-icon">${SVG.calendarX}</div>
      <h3>A\u00FAn no te has inscrito en ning\u00FAn lugar</h3>
      <p>Explora los espacios disponibles y registra tu primera hora libre.</p>
      <button class="btn-outline" onclick="showVista('vista-lugares')">Explorar Lugares</button>
    </div>`;
  } else {
    activosHTML = activos.map(r => renderRegistroCard(r, r.idx, true)).join('');
  }

  let historialHTML;
  if (completados.length === 0) {
    historialHTML = `<div style="color:var(--color-sublabel);text-align:center;padding:40px;">No hay registros completados a\u00FAn.</div>`;
  } else {
    historialHTML = completados.map(r => renderRegistroCard(r, r.idx, false)).join('');
  }

  container.innerHTML = `
    <h1 style="font-size:1.8rem;font-weight:700;color:var(--color-acento);margin-bottom:4px;">Mis lugares registrados</h1>
    <p style="color:var(--color-sublabel);margin-bottom:20px;">Administra tus reservas activas y revisa el historial...</p>
    <div class="tabs-wrap">
      <button class="tab-btn activo" id="tab-btn-activos" onclick="switchTab('activos')">Activos</button>
      <button class="tab-btn" id="tab-btn-historial" onclick="switchTab('historial')">Historial</button>
    </div>
    <div id="tab-activos" class="registros-grid" style="display:grid;">${activosHTML}</div>
    <div id="tab-historial" style="display:none;">
      <div class="registros-grid">${historialHTML}</div>
    </div>`;
}

/* ═══════════════════════════════════════════
   RENDER — FAVORITOS
═══════════════════════════════════════════ */
function toggleFavorito(lugarId) {
  const lugar = LUGARES.find(l => l.id === lugarId);
  if (!lugar) return;
  const idx = STATE.favoritos.indexOf(lugarId);
  if (idx > -1) {
    STATE.favoritos.splice(idx, 1);
    showToast(lugar.nombre + ' eliminado de favoritos.', 'fallo');
  } else {
    STATE.favoritos.push(lugarId);
    showToast(lugar.nombre + ' agregado a favoritos.', 'exito');
  }
  const vista = getVistaActiva();
  if (vista === 'vista-favoritos') renderFavoritos();
  if (vista === 'vista-lugares') renderLugares();
  if (vista === 'vista-detalle-lugar') renderDetalleLugar();
}

function renderFavoritos() {
  const container = document.getElementById('dash-content-favoritos');
  if (!container) return;
  const favs = STATE.favoritos;
  const lugaresFav = LUGARES.filter(l => favs.includes(l.id));

  if (lugaresFav.length === 0) {
    container.innerHTML = `
      <h1 style="font-size:1.8rem;font-weight:700;color:var(--color-acento);margin-bottom:4px;">Lugares favoritos</h1>
      <p style="color:var(--color-sublabel);margin-bottom:24px;">Tus espacios de estudio guardados para un registro r\u00E1pido.</p>
      <div class="estado-vacio">
        <div class="estado-vacio-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
        <h3>No tienes lugares favoritos a\u00FAn</h3>
        <p>Guarda tus espacios favoritos para acceder r\u00E1pidamente a ellos.</p>
        <button class="btn-outline" onclick="showVista('vista-lugares')">\u00A1Explora el campus!</button>
      </div>`;
    return;
  }

  container.innerHTML = `
    <h1 style="font-size:1.8rem;font-weight:700;color:var(--color-acento);margin-bottom:4px;">Lugares favoritos</h1>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;">
      <p style="color:var(--color-sublabel);">Tus espacios de estudio guardados para un registro r\u00E1pido.</p>
      <span style="font-size:.82rem;color:var(--color-sublabel);">Mostrando ${lugaresFav.length} lugares guardados</span>
    </div>
    <div class="lugares-grid">
      ${lugaresFav.map(l => {
        const disponibles = l.capacidad - l.ocupados;
        return `<div class="lugar-card">
          <div class="lugar-img-wrap">
            <img class="lugar-img" src="${l.img}" alt="${l.nombre}" loading="lazy" />
            ${renderFavoriteButton(l.id)}
            <span class="badge-disp ${l.disponible ? 'disponible' : 'lleno'} lugar-badge-disp">${l.disponible ? '\u25CF Disponible' : '\u25CF Lleno'}</span>
          </div>
          <div class="lugar-body">
            <span class="lugar-tipo">${l.tipo}</span>
            <h3 class="lugar-nombre">${l.nombre}</h3>
            <p style="font-size:.8rem;color:var(--color-sublabel);margin-bottom:8px;">${l.disponible ? disponibles + ' cupos disponibles' : 'Libera a las ' + l.horario.split(' - ')[1]}</p>
            <p class="lugar-desc">${l.desc}</p>
            <button class="btn-lugar ${l.disponible ? 'disponible' : 'lleno'}"
              onclick="${l.disponible ? `verDetalleLugar(${l.id})` : ''}">
              ${l.disponible ? 'Registrarme \u2192' : 'Reservar Turno'}
            </button>
          </div>
        </div>`;
      }).join('')}
    </div>`;
}

/* ═══════════════════════════════════════════
   RENDER — PERFIL
═══════════════════════════════════════════ */
function renderPerfil() {
  const container = document.getElementById('dash-content-perfil');
  if (!container) return;
  const u = STATE.usuario;
  const pendientes = u.hlTotal - u.hlCompletadas;
  const pct = Math.round((u.hlCompletadas / u.hlTotal) * 100);

  const historialRows = STATE.historialHL.map(h => `<tr>
    <td>${h.fecha}</td>
    <td>${h.lugar}</td>
    <td>${h.actividad}</td>
    <td class="horas-col">+${h.horas}</td>
  </tr>`).join('');

  container.innerHTML = `
    <h1 style="font-size:1.8rem;font-weight:700;color:var(--color-acento);margin-bottom:4px;">Perfil del estudiante</h1>
    <p style="color:var(--color-sublabel);margin-bottom:28px;">Consulta tu información académica y revisa tu progreso.</p>
    <div class="perfil-grid">
      <div class="perfil-card" style="text-align:center;">
        <div class="perfil-avatar">${avatarMarkup('avatar-xl')}</div>
        <div class="perfil-nombre">${u.nombre}</div>
        <div class="perfil-fila">
          <span class="perfil-fila-label">C\u00F3digo</span>
          <span class="perfil-fila-valor">${u.codigo}</span>
        </div>
        <div class="perfil-fila">
          <span class="perfil-fila-label">Correo</span>
          <span class="perfil-fila-valor">${u.correo}${CONFIG.dominioCorreo}</span>
        </div>
        <div class="perfil-fila">
          <span class="perfil-fila-label">Programa</span>
          <span class="perfil-fila-valor">${u.programa}</span>
        </div>
        <div class="perfil-fila">
          <span class="perfil-fila-label">Semestre</span>
          <span class="perfil-fila-valor">${u.semestre}</span>
        </div>
        <button class="btn-editar-perfil" onclick="abrirPerfilModal()">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
          Cambiar foto
        </button>
        <p class="perfil-lock-note">Los datos académicos quedan fijos después del registro.</p>
      </div>
      <div>
        <div class="card-stat" style="margin-bottom:20px;">
          <h3 style="font-size:1rem;font-weight:700;color:var(--color-acento);margin-bottom:16px;">Resumen de Horas Libres (HL)</h3>
          <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;">
            <div class="card-stat" style="padding:14px;gap:2px;">
              <span class="card-stat-label">Total Requeridas</span>
              <span class="card-stat-valor">${u.hlTotal}</span>
            </div>
            <div class="card-stat" style="padding:14px;gap:2px;">
              <span class="card-stat-label">Completadas</span>
              <span class="card-stat-valor cyan">${u.hlCompletadas}</span>
            </div>
            <div class="card-stat" style="padding:14px;gap:2px;">
              <span class="card-stat-label">Pendientes</span>
              <span class="card-stat-valor rojo">${pendientes}</span>
            </div>
          </div>
          <div class="progress-bar-wrap">
            <div class="progress-label">
              <span>Progreso General</span>
              <span class="pct">${pct}%</span>
            </div>
            <div class="progress-bar-track">
              <div class="progress-bar-fill" style="width:${pct}%"></div>
            </div>
          </div>
        </div>
        <div class="card-stat">
          <h3 style="font-size:1rem;font-weight:700;color:var(--color-acento);margin-bottom:16px;">Historial de Lugares Completados</h3>
          <div class="historial-table-wrap">
            <table class="tabla-historial">
              <thead><tr><th>Fecha</th><th>Lugar</th><th>Actividad</th><th>Horas</th></tr></thead>
              <tbody>${historialRows}</tbody>
            </table>
          </div>
        </div>
      </div>
    </div>`;
}

function abrirPerfilModal() {
  const modal = document.getElementById('modal-perfil');
  if (!modal) return;
  fotoPerfilTemporal = STATE.usuario.fotoPerfil || '';
  const input = document.getElementById('foto-perfil-input');
  if (input) input.value = '';
  renderFotoPreviewModal();
  modal.classList.add('visible');
  document.body.style.overflow = 'hidden';
}

function cerrarPerfilModal() {
  const modal = document.getElementById('modal-perfil');
  if (modal) modal.classList.remove('visible');
  fotoPerfilTemporal = '';
  document.body.style.overflow = '';
}

function renderFotoPreviewModal() {
  const preview = document.getElementById('foto-preview-modal');
  if (!preview) return;
  preview.innerHTML = fotoPerfilTemporal
    ? `<img class="avatar-img avatar-xl" src="${fotoPerfilTemporal}" alt="Nueva foto de perfil" />`
    : avatarMarkup('avatar-xl');
}

function previewFotoPerfil(event) {
  const file = event.target.files && event.target.files[0];
  if (!file) return;
  if (!file.type.startsWith('image/')) {
    showToast('Selecciona un archivo de imagen.', 'fallo');
    return;
  }
  const reader = new FileReader();
  reader.onload = e => {
    fotoPerfilTemporal = e.target.result;
    renderFotoPreviewModal();
  };
  reader.readAsDataURL(file);
}

function guardarFotoPerfil() {
  STATE.usuario.fotoPerfil = fotoPerfilTemporal;
  cerrarPerfilModal();
  updateUserLabels();
  setHeaderDashboard();
  renderPerfil();
  showToast('Foto de perfil actualizada.', 'exito');
}

/* ═══════════════════════════════════════════
   RENDER — HORARIO
═══════════════════════════════════════════ */
function renderHorario() {
  const container = document.getElementById('dash-content-horario');
  if (!container) return;

  const today = new Date();
  const year = today.getFullYear();
  const month = today.getMonth();
  const monthName = today.toLocaleDateString('es-ES', { month: 'long', year: 'numeric' });
  const firstDay = new Date(year, month, 1);
  const startOffset = (firstDay.getDay() + 6) % 7;
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  const activeRegs = STATE.registros.filter(r => r.estado === 'activo' && r.fechaISO && r.fechaISO.startsWith(`${year}-${String(month + 1).padStart(2, '0')}`));
  if (!STATE.diaHorarioSeleccionado && activeRegs.length) STATE.diaHorarioSeleccionado = activeRegs[0].fechaISO;

  const cells = [];
  for (let i = 0; i < startOffset; i++) cells.push('<div class="calendar-day muted"></div>');
  for (let day = 1; day <= daysInMonth; day++) {
    const iso = `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
    const regs = activeRegs.filter(r => r.fechaISO === iso);
    const isToday = iso === toISODate(today);
    const selected = iso === STATE.diaHorarioSeleccionado;
    cells.push(`
      <button class="calendar-day${regs.length ? ' has-event' : ''}${isToday ? ' today' : ''}${selected ? ' selected' : ''}" onclick="seleccionarDiaHorario('${iso}')">
        <span class="calendar-day-number">${day}</span>
        ${regs.slice(0, 2).map(r => `<span class="calendar-event-dot">${r.nombre}</span>`).join('')}
      </button>`);
  }

  const selectedRegs = activeRegs.filter(r => r.fechaISO === STATE.diaHorarioSeleccionado);
  const detailHTML = selectedRegs.length ? selectedRegs.map(r => `
    <article class="schedule-detail-card">
      <span class="reg-tipo">${r.tipo}</span>
      <h3>${r.nombre}</h3>
      <p>${SVG.calendar} ${r.fecha} · ${r.hora}</p>
      <span class="badge-disp disponible">● Activo</span>
    </article>`).join('') : `
    <div class="estado-vacio schedule-empty">
      <div class="estado-vacio-icon">${SVG.calendarX}</div>
      <h3>No hay reservas en este día</h3>
      <p>Selecciona un día marcado o explora espacios para reservar nuevas horas libres.</p>
      <button class="btn-outline" onclick="showVista('vista-lugares')">Explorar Lugares</button>
    </div>`;

  container.innerHTML = `
    <div class="dash-heading-row">
      <div>
        <h1 style="font-size:1.8rem;font-weight:700;color:var(--color-acento);margin-bottom:4px;">Mi horario</h1>
        <p style="color:var(--color-sublabel);">Reservas activas del mes y detalle por día.</p>
      </div>
      <button class="btn-outline" onclick="showVista('vista-lugares')">Nueva reserva</button>
    </div>
    <div class="schedule-layout">
      <section class="calendar-card" aria-label="Calendario de reservas">
        <div class="calendar-header">
          <h2>${monthName.charAt(0).toUpperCase() + monthName.slice(1)}</h2>
          <span>${activeRegs.length} reservas activas</span>
        </div>
        <div class="calendar-weekdays">
          <span>Lun</span><span>Mar</span><span>Mié</span><span>Jue</span><span>Vie</span><span>Sáb</span><span>Dom</span>
        </div>
        <div class="calendar-grid">${cells.join('')}</div>
      </section>
      <aside class="schedule-panel">
        <h2>Detalle del día</h2>
        ${detailHTML}
      </aside>
    </div>`;
}

function seleccionarDiaHorario(iso) {
  STATE.diaHorarioSeleccionado = iso;
  renderHorario();
}

document.addEventListener('DOMContentLoaded', () => {
  setHeaderDefault();
  bindStaticControls();
});

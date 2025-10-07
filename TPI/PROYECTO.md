# SimuladorIncidentes

## Descripción del proyecto

El proyecto consiste en el desarrollo de un simulador de emergencias urbanas con logística de respuesta automática, orientado a representar de forma realista y visual cómo distintas unidades de emergencia (como bomberos, ambulancias o cuadrillas eléctricas) actúan ante situaciones críticas en una ciudad. La aplicación ofrece a los usuarios la posibilidad de registrar incidentes, como incendios, accidentes de tránsito o cortes de luz, y tiene como objetivo gestionar y asignar los recursos disponibles de forma óptima, teniendo en cuenta la gravedad de cada evento, su localización y las condiciones del tráfico urbano simulado.

## Diagrama Entidad - Relación

<img width="886" height="750" alt="image" src="https://github.com/user-attachments/assets/e6d2c6e6-c5e6-4046-b065-b28cf2ab6fd0" />


## Bosquejo de Arquitectura

El sistema adopta una arquitectura en tres capas (Presentación, Negocio y Datos), bajo el patrón Cliente-Servidor.
El frontend (cliente web) interactúa con el backend Django REST Framework (servidor de APIs), que a su vez se comunica con la base de datos para almacenar usuarios e incidentes.

Descripción general de la interacción:

1. El usuario accede al mapa desde el navegador.
2. El frontend envía peticiones HTTP al backend (/api/...) para registrar usuarios, iniciar sesión y reportar incidentes.
3. El backend Django valida la autenticación JWT y procesa la lógica de negocio.
4. Los datos se almacenan y consultan en una base de datos relacional (MySQL).
5. Los tokens JWT permiten sesiones seguras y separación entre usuarios autenticados y no autenticados.

<img width="1024" height="1536" alt="Diagrama de arquitectura de incidentes" src="https://github.com/user-attachments/assets/e2e3dff5-7aea-4557-a603-97896ded5ce2" />

## Requerimientos

Definir los requerimientos del sistema.

### Funcionales

R01. El sistema debe permitir registrar nuevos usuarios proporcionando nombre, apellido, email, contraseña y rol.
R02. El sistema debe permitir iniciar sesión con email y contraseña.
R03. El sistema debe permitir cerrar sesión y eliminar el token de autenticación.
R04. El sistema debe diferenciar los roles de usuario (Administrador, Operador, Usuario).
R05. El sistema debe autenticar mediante tokens JWT a los usuarios que acceden a funciones protegidas.
R06. El sistema debe mostrar en un mapa todos los incidentes registrados con su título, descripción y ubicación.
R07. El sistema debe permitir que los usuarios autenticados reporten un nuevo incidente haciendo clic en el mapa.
R08. El sistema debe permitir visualizar todos los incidentes en el mapa mediante marcadores.
R09. El sistema debe validar que solo los usuarios autenticados puedan crear incidentes.
R10. El sistema debe registrar la fecha y ubicación del incidente al momento de su creación.
R11. El sistema debe permitir a los administradores consultar todos los incidentes registrados.

### No Funcionales

Listado y descripción breve de los requerimientos no funcionales. Utilizar las categorias dadas:

### Portability

**Obligatorios**

- El sistema debe funcionar correctamente en múltiples navegadores (Sólo Web).
- El sistema debe ejecutarse desde un único archivo .py llamado app.py (Sólo Escritorio).
  
### Security

**Obligatorios**

- Todas las contraseñas deben guardarse con encriptado criptográfico (SHA o equivalente).
- Todas los Tokens / API Keys o similares no deben exponerse de manera pública.
- Solo usuarios autenticados pueden enviar datos al endpoint de incidentes.

### Maintainability

**Obligatorios**

- El sistema debe diseñarse con la arquitectura en 3 capas. Presentación (frontend), Negocio (Django + lógica de negocio), Datos (ORM y DB).
- El sistema debe utilizar control de versiones mediante GIT (GitHub).
- Se utiliza Python 3.12 y Django REST Framework, con código modular por dominio (usuarios, incidentes, recursos, rutas, etc).

### Reliability

- El sistema debe mantener la sesión activa mientras el token JWT sea válido.
- Si el token expira, el usuario debe volver a autenticarse.

### Scalability

**Obligatorios**

- El sistema debe funcionar desde una ventana normal y una de incógnito de manera independiente (Sólo Web).
  - Aclaración: No se debe guardar el usuario en una variable local, deben usarse Tokens, Cookies o similares.
- Puede escalarse fácilmente mediante contenedores o instancias adicionales del servidor web.

### Performance

**Obligatorios**

- El sistema debe responder a las peticiones de login y carga del mapa en menos de 3 segundos en un equipo hogareño.
- La API REST debe optimizar consultas a base de datos mediante ORM.

### Reusability

- Los componentes del backend (views, serializers, modelos) están desacoplados y reutilizables en otros proyectos Django.

### Flexibility

**Obligatorios**

- El sistema debe utilizar una base de datos SQL o NoSQL.
- El sistema utiliza una base de datos relacional (MySQL) y puede cambiarse fácilmente mediante configuración en settings.py.

## Stack Tecnológico

### Capa de Datos

Base de datos: MySQL.

ORM: Django ORM.

Motivo: permite manejo sencillo de modelos, migraciones automáticas y consultas seguras sin SQL directo.

### Capa de Negocio

Framework: Django REST Framework.

Autenticación: rest_framework_simplejwt para gestión de tokens JWT.

Motivo: separación clara entre endpoints, control de permisos y serialización de datos.

### Capa de Presentación

Frontend: HTML, CSS y JavaScript nativo (puede integrarse con frameworks como Vue o React en el futuro).

Mapa: integración con Leaflet.js para mostrar incidentes geolocalizados.

Motivo: simplicidad, rendimiento y soporte en todos los navegadores modernos.

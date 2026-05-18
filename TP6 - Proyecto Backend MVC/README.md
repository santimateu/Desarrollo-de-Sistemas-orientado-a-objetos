# TP6 - Gestión de Alumnos y Cursos (Microservicios MVC)

## Arquitectura
3 microservicios independientes. Cada uno corre en su propio puerto y no importa archivos de los otros.

```
alumno-service/      → puerto 3001
curso-service/       → puerto 3002
inscripcion-service/ → puerto 3003
```

Cada servicio tiene su propia estructura MVC:
```
src/
├── controllers/
├── domain/
├── routes/
├── services/
├── dao/
├── app.js
└── index.js
```

---

## Cómo ejecutar

Cada servicio se instala y ejecuta por separado (abrir 3 terminales):

Abrir 3 terminales separadas. En cada una ejecutar los dos comandos uno por uno:

**Terminal 1:**
```powershell
cd alumno-service
npm install
npm start
```

**Terminal 2:**
```powershell
cd curso-service
npm install
npm start
```

**Terminal 3:**
```powershell
cd inscripcion-service
npm install
npm start
```

---

## Endpoints

### alumno-service (puerto 3001)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /alumnos | Listar todos |
| GET | /alumnos/:id | Obtener por ID |
| POST | /alumnos | Crear alumno |
| PUT | /alumnos/:id | Actualizar alumno |
| DELETE | /alumnos/:id | Eliminar alumno |

### curso-service (puerto 3002)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /cursos | Listar todos |
| GET | /cursos/:id | Obtener por ID |
| POST | /cursos | Crear curso |
| PUT | /cursos/:id | Actualizar curso |
| DELETE | /cursos/:id | Eliminar curso |

### inscripcion-service (puerto 3003)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /inscripciones | Listar todas |
| GET | /inscripciones/:id | Obtener por ID |
| POST | /inscripciones | Registrar inscripción |
| PUT | /inscripciones/:id/baja | Dar de baja |
| DELETE | /inscripciones/:id | Eliminar inscripción |

---

## Reglas de negocio (inscripcion-service)

1. Un alumno no puede tener más de **5 inscripciones activas**.
2. Un alumno no puede inscribirse **dos veces** al mismo curso.
3. Un curso no puede superar su **cupo máximo**.

---

## Ejemplos con curl

### Crear alumno
```bash
curl -X POST http://localhost:3001/alumnos \
  -H "Content-Type: application/json" \
  -d '{"nombre": "María López", "email": "maria@mail.com"}'
```

### Crear curso
```bash
curl -X POST http://localhost:3002/cursos \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Física I", "descripcion": "Mecánica clásica", "cupoMaximo": 20}'
```

### Inscribir alumno en curso
```bash
curl -X POST http://localhost:3003/inscripciones \
  -H "Content-Type: application/json" \
  -d '{"alumnoId": 1, "cursoId": 1, "cupoMaximoCurso": 30}'
```

### Dar de baja una inscripción
```bash
curl -X PUT http://localhost:3003/inscripciones/1/baja
```

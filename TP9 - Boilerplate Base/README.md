# TP9 - Boilerplate Base

## Estructura

```
backend/                     → puerto 3001
└── src/
    ├── domain/              → entidades (clases)
    ├── dao/                 → acceso a datos (en memoria, simula la BD)
    ├── services/            → lógica de negocio y validaciones
    ├── controllers/         → reciben el request y arman la respuesta HTTP
    ├── routes/              → definen los endpoints
    ├── app.js               → configura Express y registra las rutas
    └── index.js             → levanta el servidor

frontend/                    → puerto 3000
└── src/
    ├── models/              → estructura/valores por defecto de cada entidad
    ├── services/            → llamadas HTTP al backend (fetch)
    ├── controllers/         → hooks de React con el estado y las acciones
    ├── components/          → vistas (Header, Footer, ItemsView)
    ├── App.jsx              → tabs y navegación
    └── index.jsx            → punto de entrada
```

Flujo de una petición: `route → controller → service → dao → domain`.

## Cómo ejecutar

Abrir 2 terminales:

**Terminal 1 - backend:**
```powershell
cd backend
npm install
npm start          # o npm run dev para recarga automática (nodemon)
```

**Terminal 2 - frontend:**
```powershell
cd frontend
npm install
npm run dev
```

Abrir http://localhost:3000. El puerto del backend se puede cambiar con la variable `PORT` (si lo cambiás, actualizá también `BASE` en `frontend/src/services/itemService.js`).

## Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /health | Estado del servidor |
| GET | /items | Listar todos |
| GET | /items/:id | Obtener por ID |
| POST | /items | Crear item |
| PUT | /items/:id | Actualizar item |
| DELETE | /items/:id | Eliminar item |

```bash
curl -X POST http://localhost:3001/items \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Mi item", "descripcion": "Prueba"}'
```

## Convenciones

- El **service** devuelve `{ data }` si salió bien o `{ error }` si falló; el **controller** traduce eso a un status HTTP (400 / 404 / 201).
- Los ids llegan como string por la URL, el service los convierte con `Number(id)`.
- El **dao** guarda los datos en un array en memoria: se pierden al reiniciar el servidor.

## Cómo agregar una nueva entidad

Ejemplo con `Alumno`. Copiar los archivos de `Item` y renombrarlos:

**Backend**
1. `domain/alumnoDomain.js` → clase con los campos.
2. `dao/alumnoDao.js` → `getAll`, `getById`, `create`, `update`, `remove`.
3. `services/alumnoService.js` → validaciones y reglas de negocio.
4. `controllers/alumnoController.js` → traduce el resultado del service a HTTP.
5. `routes/alumnoRoutes.js` → endpoints.
6. En `app.js`: `app.use('/alumnos', require('./routes/alumnoRoutes'));`

**Frontend**
1. `models/alumnoModel.js`, `services/alumnoService.js`, `controllers/alumnoController.js` (hook `useAlumnos`).
2. `components/AlumnosView.jsx`.
3. En `App.jsx`: agregar la entrada en `tabs` y renderizar la vista.

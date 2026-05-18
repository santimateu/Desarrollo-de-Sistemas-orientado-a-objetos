const BASE = 'http://localhost:3001/alumnos';

export const getAlumnos  = ()       => fetch(BASE).then(r => r.json());
export const getAlumno   = (id)     => fetch(`${BASE}/${id}`).then(r => r.json());
export const createAlumno = (data)  => fetch(BASE, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data),
}).then(r => r.json());
export const updateAlumno = (id, data) => fetch(`${BASE}/${id}`, {
  method: 'PUT',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data),
}).then(r => r.json());
export const deleteAlumno = (id) => fetch(`${BASE}/${id}`, { method: 'DELETE' }).then(r => r.json());

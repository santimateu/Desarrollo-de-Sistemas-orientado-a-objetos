const BASE = 'http://localhost:3003/inscripciones';

export const getInscripciones   = ()     => fetch(BASE).then(r => r.json());
export const getInscripcion     = (id)   => fetch(`${BASE}/${id}`).then(r => r.json());
export const createInscripcion  = (data) => fetch(BASE, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data),
}).then(r => r.json());
export const darBajaInscripcion = (id)   => fetch(`${BASE}/${id}/baja`, { method: 'PUT' }).then(r => r.json());
export const deleteInscripcion  = (id)   => fetch(`${BASE}/${id}`, { method: 'DELETE' }).then(r => r.json());

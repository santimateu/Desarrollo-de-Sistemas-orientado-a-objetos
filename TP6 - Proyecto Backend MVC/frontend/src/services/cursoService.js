const BASE = 'http://localhost:3002/cursos';

export const getCursos   = ()       => fetch(BASE).then(r => r.json());
export const getCurso    = (id)     => fetch(`${BASE}/${id}`).then(r => r.json());
export const createCurso = (data)   => fetch(BASE, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data),
}).then(r => r.json());
export const updateCurso = (id, data) => fetch(`${BASE}/${id}`, {
  method: 'PUT',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data),
}).then(r => r.json());
export const deleteCurso = (id) => fetch(`${BASE}/${id}`, { method: 'DELETE' }).then(r => r.json());

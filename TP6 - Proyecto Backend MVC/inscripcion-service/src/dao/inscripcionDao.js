const Inscripcion = require('../domain/inscripcionDomain');

let inscripciones = [];
let nextId = 1;

const getAll = () => inscripciones;

const getById = (id) => inscripciones.find(i => i.id === id);

const getActivasByAlumno = (alumnoId) =>
  inscripciones.filter(i => i.alumnoId === alumnoId && i.estado === 'activa');

const getActivasByCurso = (cursoId) =>
  inscripciones.filter(i => i.cursoId === cursoId && i.estado === 'activa');

const findDuplicado = (alumnoId, cursoId) =>
  inscripciones.find(i => i.alumnoId === alumnoId && i.cursoId === cursoId && i.estado === 'activa');

const create = (alumnoId, cursoId, cupoMaximoCurso) => {
  const inscripcion = new Inscripcion(nextId++, alumnoId, cursoId, cupoMaximoCurso);
  inscripciones.push(inscripcion);
  return inscripcion;
};

const update = (id, datos) => {
  const inscripcion = getById(id);
  if (!inscripcion) return null;
  Object.assign(inscripcion, datos);
  return inscripcion;
};

const remove = (id) => {
  const index = inscripciones.findIndex(i => i.id === id);
  if (index === -1) return false;
  inscripciones.splice(index, 1);
  return true;
};

module.exports = {
  getAll, getById, getActivasByAlumno, getActivasByCurso,
  findDuplicado, create, update, remove,
};

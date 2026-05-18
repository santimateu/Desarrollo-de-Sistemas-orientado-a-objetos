const alumnoDao = require('../dao/alumnoDao');

const getAll = () => alumnoDao.getAll();

const getById = (id) => alumnoDao.getById(Number(id));

const create = (nombre, email, estado = 'activo') => {
  if (!nombre || !email) return { error: 'Faltan campos: nombre, email' };
  return { data: alumnoDao.create(nombre, email, estado) };
};

const update = (id, datos) => {
  const alumno = alumnoDao.update(Number(id), datos);
  if (!alumno) return { error: 'Alumno no encontrado' };
  return { data: alumno };
};

const remove = (id) => {
  const ok = alumnoDao.remove(Number(id));
  if (!ok) return { error: 'Alumno no encontrado' };
  return { data: true };
};

module.exports = { getAll, getById, create, update, remove };

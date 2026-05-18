const cursoDao = require('../dao/cursoDao');

const getAll = () => cursoDao.getAll();

const getById = (id) => cursoDao.getById(Number(id));

const create = (nombre, descripcion, cupoMaximo, estado) => {
  if (!nombre || !cupoMaximo) return { error: 'Faltan campos: nombre, cupoMaximo' };
  return { data: cursoDao.create(nombre, descripcion, Number(cupoMaximo), estado) };
};

const update = (id, datos) => {
  const curso = cursoDao.update(Number(id), datos);
  if (!curso) return { error: 'Curso no encontrado' };
  return { data: curso };
};

const remove = (id) => {
  const ok = cursoDao.remove(Number(id));
  if (!ok) return { error: 'Curso no encontrado' };
  return { data: true };
};

module.exports = { getAll, getById, create, update, remove };

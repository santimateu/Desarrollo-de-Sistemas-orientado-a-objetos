const itemDao = require('../dao/itemDao');

// Las reglas de negocio y validaciones van en el service.
// Devuelve { data } si salió bien o { error } si falló.

const getAll = () => itemDao.getAll();

const getById = (id) => itemDao.getById(Number(id));

const create = (nombre, descripcion = '', estado = 'activo') => {
  if (!nombre) return { error: 'Faltan campos: nombre' };
  return { data: itemDao.create(nombre, descripcion, estado) };
};

const update = (id, datos) => {
  const item = itemDao.update(Number(id), datos);
  if (!item) return { error: 'Item no encontrado' };
  return { data: item };
};

const remove = (id) => {
  const ok = itemDao.remove(Number(id));
  if (!ok) return { error: 'Item no encontrado' };
  return { data: true };
};

module.exports = { getAll, getById, create, update, remove };

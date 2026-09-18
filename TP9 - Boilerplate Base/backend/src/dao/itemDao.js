const Item = require('../domain/itemDomain');

// Simula la base de datos en memoria
let items = [
  new Item(1, 'Item de ejemplo', 'Primer item de prueba', 'activo'),
  new Item(2, 'Otro item', 'Segundo item de prueba', 'inactivo'),
];

let nextId = 3;

const getAll = () => items;

const getById = (id) => items.find(i => i.id === id);

const create = (nombre, descripcion, estado) => {
  const item = new Item(nextId++, nombre, descripcion, estado);
  items.push(item);
  return item;
};

const update = (id, datos) => {
  const item = getById(id);
  if (!item) return null;
  Object.assign(item, datos);
  return item;
};

const remove = (id) => {
  const index = items.findIndex(i => i.id === id);
  if (index === -1) return false;
  items.splice(index, 1);
  return true;
};

module.exports = { getAll, getById, create, update, remove };

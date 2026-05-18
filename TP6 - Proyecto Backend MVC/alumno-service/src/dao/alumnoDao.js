const Alumno = require('../domain/alumnoDomain');

let alumnos = [
  new Alumno(1, 'Juan Pérez', 'juan@mail.com', 'activo'),
  new Alumno(2, 'Ana García', 'ana@mail.com', 'activo'),
  new Alumno(3, 'Pedro López', 'pedro@mail.com', 'inactivo'),
];

let nextId = 4;

const getAll = () => alumnos;

const getById = (id) => alumnos.find(a => a.id === id);

const create = (nombre, email, estado) => {
  const alumno = new Alumno(nextId++, nombre, email, estado);
  alumnos.push(alumno);
  return alumno;
};

const update = (id, datos) => {
  const alumno = getById(id);
  if (!alumno) return null;
  Object.assign(alumno, datos);
  return alumno;
};

const remove = (id) => {
  const index = alumnos.findIndex(a => a.id === id);
  if (index === -1) return false;
  alumnos.splice(index, 1);
  return true;
};

module.exports = { getAll, getById, create, update, remove };

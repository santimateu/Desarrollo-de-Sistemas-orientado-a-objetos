const Curso = require('../domain/cursoDomain');

let cursos = [
  new Curso(1, 'Matemáticas I', 'Álgebra y cálculo básico', 30),
  new Curso(2, 'Programación I', 'Introducción a la programación', 25),
  new Curso(3, 'Historia', 'Historia mundial moderna', 20, 'cerrado'),
];

let nextId = 4;

const getAll = () => cursos;

const getById = (id) => cursos.find(c => c.id === id);

const create = (nombre, descripcion, cupoMaximo, estado) => {
  const curso = new Curso(nextId++, nombre, descripcion, cupoMaximo, estado);
  cursos.push(curso);
  return curso;
};

const update = (id, datos) => {
  const curso = getById(id);
  if (!curso) return null;
  Object.assign(curso, datos);
  return curso;
};

const remove = (id) => {
  const index = cursos.findIndex(c => c.id === id);
  if (index === -1) return false;
  cursos.splice(index, 1);
  return true;
};

module.exports = { getAll, getById, create, update, remove };

const cursoService = require('../services/cursoService');

const getAll = (req, res) => {
  res.json(cursoService.getAll());
};

const getById = (req, res) => {
  const curso = cursoService.getById(req.params.id);
  if (!curso) return res.status(404).json({ error: 'Curso no encontrado' });
  res.json(curso);
};

const create = (req, res) => {
  const { nombre, descripcion, cupoMaximo, estado } = req.body;
  const resultado = cursoService.create(nombre, descripcion, cupoMaximo, estado);
  if (resultado.error) return res.status(400).json({ error: resultado.error });
  res.status(201).json(resultado.data);
};

const update = (req, res) => {
  const resultado = cursoService.update(req.params.id, req.body);
  if (resultado.error) return res.status(404).json({ error: resultado.error });
  res.json(resultado.data);
};

const remove = (req, res) => {
  const resultado = cursoService.remove(req.params.id);
  if (resultado.error) return res.status(404).json({ error: resultado.error });
  res.json({ mensaje: 'Curso eliminado' });
};

module.exports = { getAll, getById, create, update, remove };

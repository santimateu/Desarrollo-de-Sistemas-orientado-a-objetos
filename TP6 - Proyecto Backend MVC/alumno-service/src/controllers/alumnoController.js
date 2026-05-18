const alumnoService = require('../services/alumnoService');

const getAll = (req, res) => {
  res.json(alumnoService.getAll());
};

const getById = (req, res) => {
  const alumno = alumnoService.getById(req.params.id);
  if (!alumno) return res.status(404).json({ error: 'Alumno no encontrado' });
  res.json(alumno);
};

const create = (req, res) => {
  const { nombre, email, estado } = req.body;
  const resultado = alumnoService.create(nombre, email, estado);
  if (resultado.error) return res.status(400).json({ error: resultado.error });
  res.status(201).json(resultado.data);
};

const update = (req, res) => {
  const resultado = alumnoService.update(req.params.id, req.body);
  if (resultado.error) return res.status(404).json({ error: resultado.error });
  res.json(resultado.data);
};

const remove = (req, res) => {
  const resultado = alumnoService.remove(req.params.id);
  if (resultado.error) return res.status(404).json({ error: resultado.error });
  res.json({ mensaje: 'Alumno eliminado' });
};

module.exports = { getAll, getById, create, update, remove };

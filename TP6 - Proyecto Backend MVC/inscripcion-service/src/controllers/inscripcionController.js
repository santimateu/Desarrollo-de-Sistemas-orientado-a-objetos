const inscripcionService = require('../services/inscripcionService');

const getAll = (req, res) => {
  res.json(inscripcionService.getAll());
};

const getById = (req, res) => {
  const inscripcion = inscripcionService.getById(req.params.id);
  if (!inscripcion) return res.status(404).json({ error: 'Inscripción no encontrada' });
  res.json(inscripcion);
};

const create = (req, res) => {
  const { alumnoId, cursoId, cupoMaximoCurso } = req.body;
  const resultado = inscripcionService.create(alumnoId, cursoId, cupoMaximoCurso);
  if (resultado.error) return res.status(400).json({ error: resultado.error });
  res.status(201).json(resultado.data);
};

const darBaja = (req, res) => {
  const resultado = inscripcionService.darBaja(req.params.id);
  if (resultado.error) return res.status(400).json({ error: resultado.error });
  res.json({ mensaje: 'Inscripción dada de baja', inscripcion: resultado.data });
};

const remove = (req, res) => {
  const resultado = inscripcionService.remove(req.params.id);
  if (resultado.error) return res.status(404).json({ error: resultado.error });
  res.json({ mensaje: 'Inscripción eliminada' });
};

module.exports = { getAll, getById, create, darBaja, remove };

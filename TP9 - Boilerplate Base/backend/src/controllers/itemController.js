const itemService = require('../services/itemService');

const getAll = (req, res) => {
  res.json(itemService.getAll());
};

const getById = (req, res) => {
  const item = itemService.getById(req.params.id);
  if (!item) return res.status(404).json({ error: 'Item no encontrado' });
  res.json(item);
};

const create = (req, res) => {
  const { nombre, descripcion, estado } = req.body;
  const resultado = itemService.create(nombre, descripcion, estado);
  if (resultado.error) return res.status(400).json({ error: resultado.error });
  res.status(201).json(resultado.data);
};

const update = (req, res) => {
  const resultado = itemService.update(req.params.id, req.body);
  if (resultado.error) return res.status(404).json({ error: resultado.error });
  res.json(resultado.data);
};

const remove = (req, res) => {
  const resultado = itemService.remove(req.params.id);
  if (resultado.error) return res.status(404).json({ error: resultado.error });
  res.json({ mensaje: 'Item eliminado' });
};

module.exports = { getAll, getById, create, update, remove };

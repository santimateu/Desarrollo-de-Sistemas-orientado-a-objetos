const inscripcionDao = require('../dao/inscripcionDao');

const MAX_INSCRIPCIONES_POR_ALUMNO = 5;

const getAll = () => inscripcionDao.getAll();

const getById = (id) => inscripcionDao.getById(Number(id));

// Reglas de negocio al inscribir un alumno
const create = (alumnoId, cursoId, cupoMaximoCurso) => {
  if (!alumnoId || !cursoId || !cupoMaximoCurso)
    return { error: 'Faltan campos: alumnoId, cursoId, cupoMaximoCurso' };

  // Regla 1: no puede tener más de 5 inscripciones activas
  const inscripcionesAlumno = inscripcionDao.getActivasByAlumno(Number(alumnoId));
  if (inscripcionesAlumno.length >= MAX_INSCRIPCIONES_POR_ALUMNO)
    return { error: `El alumno ya tiene ${MAX_INSCRIPCIONES_POR_ALUMNO} inscripciones activas` };

  // Regla 2: no puede inscribirse dos veces al mismo curso
  const duplicado = inscripcionDao.findDuplicado(Number(alumnoId), Number(cursoId));
  if (duplicado)
    return { error: 'El alumno ya está inscripto en este curso' };

  // Regla 3: el curso no puede superar su cupo máximo
  const inscripcionesCurso = inscripcionDao.getActivasByCurso(Number(cursoId));
  if (inscripcionesCurso.length >= Number(cupoMaximoCurso))
    return { error: 'El curso no tiene cupo disponible' };

  return { data: inscripcionDao.create(Number(alumnoId), Number(cursoId), Number(cupoMaximoCurso)) };
};

// Dar de baja una inscripción
const darBaja = (id) => {
  const inscripcion = inscripcionDao.getById(Number(id));
  if (!inscripcion) return { error: 'Inscripción no encontrada' };
  if (inscripcion.estado === 'baja') return { error: 'Esta inscripción ya está dada de baja' };

  inscripcionDao.update(Number(id), { estado: 'baja' });
  return { data: inscripcion };
};

const remove = (id) => {
  const ok = inscripcionDao.remove(Number(id));
  if (!ok) return { error: 'Inscripción no encontrada' };
  return { data: true };
};

module.exports = { getAll, getById, create, darBaja, remove };

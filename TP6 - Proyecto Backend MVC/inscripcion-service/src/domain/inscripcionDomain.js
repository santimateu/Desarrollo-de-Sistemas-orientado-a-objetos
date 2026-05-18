class Inscripcion {
  constructor(id, alumnoId, cursoId, cupoMaximoCurso) {
    this.id = id;
    this.alumnoId = alumnoId;
    this.cursoId = cursoId;
    this.cupoMaximoCurso = cupoMaximoCurso;
    this.fechaInscripcion = new Date().toISOString();
    this.estado = 'activa'; // 'activa' | 'baja'
  }
}

module.exports = Inscripcion;

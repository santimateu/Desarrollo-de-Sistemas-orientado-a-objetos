class Curso {
  constructor(id, nombre, descripcion, cupoMaximo, estado = 'abierto') {
    this.id = id;
    this.nombre = nombre;
    this.descripcion = descripcion;
    this.cupoMaximo = cupoMaximo;
    this.cupoDisponible = cupoMaximo;
    this.estado = estado; // 'abierto' | 'cerrado'
  }
}

module.exports = Curso;

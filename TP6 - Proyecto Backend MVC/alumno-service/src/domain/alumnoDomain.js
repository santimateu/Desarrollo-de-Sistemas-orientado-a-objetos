class Alumno {
  constructor(id, nombre, email, estado = 'activo') {
    this.id = id;
    this.nombre = nombre;
    this.email = email;
    this.estado = estado; // 'activo' | 'inactivo'
  }
}

module.exports = Alumno;

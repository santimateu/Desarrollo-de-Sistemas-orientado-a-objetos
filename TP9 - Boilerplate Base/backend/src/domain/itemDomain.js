class Item {
  constructor(id, nombre, descripcion, estado = 'activo') {
    this.id = id;
    this.nombre = nombre;
    this.descripcion = descripcion;
    this.estado = estado; // 'activo' | 'inactivo'
  }
}

module.exports = Item;

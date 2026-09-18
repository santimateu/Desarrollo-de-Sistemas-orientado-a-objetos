import { useState } from 'react';
import { useItems } from '../controllers/itemController';
import { itemDefault } from '../models/itemModel';

export default function ItemsView() {
  const { items, loading, error, crear, eliminar } = useItems();
  const [form, setForm] = useState(itemDefault);
  const [msg, setMsg]   = useState(null);

  const flash = (type, text) => {
    setMsg({ type, text });
    setTimeout(() => setMsg(null), 3000);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const r = await crear(form);
    if (r.error) flash('error', r.error);
    else { flash('success', `Item "${r.nombre}" creado`); setForm(itemDefault); }
  };

  return (
    <div>
      <h2 className="view-title">📦 Items</h2>
      <div className="view">
        <div className="card">
          {error && <div className="error-msg">{error}</div>}
          {loading && <div className="loading">Cargando items...</div>}
          {!loading && items.length === 0 && !error && (
            <div className="empty-state"><span>📭</span>No hay items registrados</div>
          )}
          {!loading && items.length > 0 && (
            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>ID</th><th>Nombre</th><th>Descripción</th><th>Estado</th><th>Acciones</th>
                  </tr>
                </thead>
                <tbody>
                  {items.map(i => (
                    <tr key={i.id}>
                      <td><span className="badge badge-gray">#{i.id}</span></td>
                      <td><strong>{i.nombre}</strong></td>
                      <td>{i.descripcion}</td>
                      <td>
                        <span className={`badge ${i.estado === 'activo' ? 'badge-green' : 'badge-red'}`}>
                          {i.estado}
                        </span>
                      </td>
                      <td>
                        <button className="btn btn-danger" onClick={() => eliminar(i.id)}>
                          🗑 Eliminar
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>

        <div className="card">
          <p className="card-title">+ Nuevo Item</p>
          {msg && <div className={msg.type === 'error' ? 'error-msg' : 'success-msg'}>{msg.text}</div>}
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Nombre</label>
              <input type="text" placeholder="Nombre del item" value={form.nombre}
                onChange={e => setForm({ ...form, nombre: e.target.value })} required />
            </div>
            <div className="form-group">
              <label>Descripción</label>
              <input type="text" placeholder="Descripción" value={form.descripcion}
                onChange={e => setForm({ ...form, descripcion: e.target.value })} />
            </div>
            <div className="form-group">
              <label>Estado</label>
              <select value={form.estado} onChange={e => setForm({ ...form, estado: e.target.value })}>
                <option value="activo">Activo</option>
                <option value="inactivo">Inactivo</option>
              </select>
            </div>
            <button type="submit" className="btn btn-primary">Crear Item</button>
          </form>
        </div>
      </div>
    </div>
  );
}

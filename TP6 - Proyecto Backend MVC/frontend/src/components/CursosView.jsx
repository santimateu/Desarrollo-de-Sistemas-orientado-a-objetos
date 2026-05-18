import { useState } from 'react';
import { useCursos } from '../controllers/cursoController';
import { cursoDefault } from '../models/cursoModel';

export default function CursosView() {
  const { cursos, loading, error, crear, eliminar } = useCursos();
  const [form, setForm] = useState(cursoDefault);
  const [msg, setMsg]   = useState(null);

  const flash = (type, text) => {
    setMsg({ type, text });
    setTimeout(() => setMsg(null), 3000);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const r = await crear(form);
    if (r.error) flash('error', r.error);
    else { flash('success', `Curso "${r.nombre}" creado`); setForm(cursoDefault); }
  };

  return (
    <div>
      <h2 className="view-title">📚 Cursos</h2>
      <div className="view">
        <div className="card">
          {error && <div className="error-msg">{error}</div>}
          {loading && <div className="loading">Cargando cursos...</div>}
          {!loading && cursos.length === 0 && !error && (
            <div className="empty-state"><span>📖</span>No hay cursos registrados</div>
          )}
          {!loading && cursos.length > 0 && (
            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>ID</th><th>Nombre</th><th>Descripción</th><th>Cupo</th><th>Estado</th><th>Acciones</th>
                  </tr>
                </thead>
                <tbody>
                  {cursos.map(c => (
                    <tr key={c.id}>
                      <td><span className="badge badge-gray">#{c.id}</span></td>
                      <td><strong>{c.nombre}</strong></td>
                      <td>{c.descripcion}</td>
                      <td>
                        <span className="badge badge-blue">
                          {c.cupoDisponible}/{c.cupoMaximo}
                        </span>
                      </td>
                      <td>
                        <span className={`badge ${c.estado === 'abierto' ? 'badge-green' : 'badge-red'}`}>
                          {c.estado}
                        </span>
                      </td>
                      <td>
                        <button className="btn btn-danger" onClick={() => eliminar(c.id)}>
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
          <p className="card-title">+ Nuevo Curso</p>
          {msg && <div className={msg.type === 'error' ? 'error-msg' : 'success-msg'}>{msg.text}</div>}
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Nombre</label>
              <input type="text" placeholder="Ej: Matemáticas I" value={form.nombre}
                onChange={e => setForm({ ...form, nombre: e.target.value })} required />
            </div>
            <div className="form-group">
              <label>Descripción</label>
              <input type="text" placeholder="Descripción breve" value={form.descripcion}
                onChange={e => setForm({ ...form, descripcion: e.target.value })} />
            </div>
            <div className="form-group">
              <label>Cupo máximo</label>
              <input type="number" min="1" value={form.cupoMaximo}
                onChange={e => setForm({ ...form, cupoMaximo: e.target.value })} required />
            </div>
            <div className="form-group">
              <label>Estado</label>
              <select value={form.estado} onChange={e => setForm({ ...form, estado: e.target.value })}>
                <option value="abierto">Abierto</option>
                <option value="cerrado">Cerrado</option>
              </select>
            </div>
            <button type="submit" className="btn btn-primary">Crear Curso</button>
          </form>
        </div>
      </div>
    </div>
  );
}

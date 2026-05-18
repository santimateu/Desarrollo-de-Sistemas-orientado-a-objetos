import { useState } from 'react';
import { useAlumnos } from '../controllers/alumnoController';
import { alumnoDefault } from '../models/alumnoModel';

export default function AlumnosView() {
  const { alumnos, loading, error, crear, eliminar } = useAlumnos();
  const [form, setForm] = useState(alumnoDefault);
  const [msg, setMsg]   = useState(null);

  const flash = (type, text) => {
    setMsg({ type, text });
    setTimeout(() => setMsg(null), 3000);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const r = await crear(form);
    if (r.error) flash('error', r.error);
    else { flash('success', `Alumno "${r.nombre}" creado`); setForm(alumnoDefault); }
  };

  return (
    <div>
      <h2 className="view-title">👨‍🎓 Alumnos</h2>
      <div className="view">
        <div className="card">
          {error && <div className="error-msg">{error}</div>}
          {loading && <div className="loading">Cargando alumnos...</div>}
          {!loading && alumnos.length === 0 && !error && (
            <div className="empty-state"><span>👤</span>No hay alumnos registrados</div>
          )}
          {!loading && alumnos.length > 0 && (
            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>ID</th><th>Nombre</th><th>Email</th><th>Estado</th><th>Acciones</th>
                  </tr>
                </thead>
                <tbody>
                  {alumnos.map(a => (
                    <tr key={a.id}>
                      <td><span className="badge badge-gray">#{a.id}</span></td>
                      <td><strong>{a.nombre}</strong></td>
                      <td>{a.email}</td>
                      <td>
                        <span className={`badge ${a.estado === 'activo' ? 'badge-green' : 'badge-red'}`}>
                          {a.estado}
                        </span>
                      </td>
                      <td>
                        <button className="btn btn-danger" onClick={() => eliminar(a.id)}>
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
          <p className="card-title">+ Nuevo Alumno</p>
          {msg && <div className={msg.type === 'error' ? 'error-msg' : 'success-msg'}>{msg.text}</div>}
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Nombre</label>
              <input type="text" placeholder="Nombre completo" value={form.nombre}
                onChange={e => setForm({ ...form, nombre: e.target.value })} required />
            </div>
            <div className="form-group">
              <label>Email</label>
              <input type="email" placeholder="correo@ejemplo.com" value={form.email}
                onChange={e => setForm({ ...form, email: e.target.value })} required />
            </div>
            <div className="form-group">
              <label>Estado</label>
              <select value={form.estado} onChange={e => setForm({ ...form, estado: e.target.value })}>
                <option value="activo">Activo</option>
                <option value="inactivo">Inactivo</option>
              </select>
            </div>
            <button type="submit" className="btn btn-primary">Crear Alumno</button>
          </form>
        </div>
      </div>
    </div>
  );
}

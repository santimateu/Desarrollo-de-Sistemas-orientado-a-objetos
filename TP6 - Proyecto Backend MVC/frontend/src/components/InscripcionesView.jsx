import { useState } from 'react';
import { useInscripciones } from '../controllers/inscripcionController';
import { inscripcionDefault } from '../models/inscripcionModel';

export default function InscripcionesView() {
  const { inscripciones, loading, error, crear, darBaja, eliminar } = useInscripciones();
  const [form, setForm] = useState(inscripcionDefault);
  const [msg, setMsg]   = useState(null);

  const flash = (type, text) => {
    setMsg({ type, text });
    setTimeout(() => setMsg(null), 4000);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const r = await crear(form);
    if (r.error) flash('error', r.error);
    else { flash('success', `Inscripción #${r.id} registrada`); setForm(inscripcionDefault); }
  };

  const handleBaja = async (id) => {
    const r = await darBaja(id);
    if (r.error) flash('error', r.error);
    else flash('success', 'Inscripción dada de baja');
  };

  return (
    <div>
      <h2 className="view-title">📋 Inscripciones</h2>
      <div className="view">
        <div className="card">
          {error && <div className="error-msg">{error}</div>}
          {loading && <div className="loading">Cargando inscripciones...</div>}
          {!loading && inscripciones.length === 0 && !error && (
            <div className="empty-state"><span>📝</span>No hay inscripciones registradas</div>
          )}
          {msg && <div className={msg.type === 'error' ? 'error-msg' : 'success-msg'}>{msg.text}</div>}
          {!loading && inscripciones.length > 0 && (
            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>ID</th><th>Alumno ID</th><th>Curso ID</th><th>Fecha</th><th>Estado</th><th>Acciones</th>
                  </tr>
                </thead>
                <tbody>
                  {inscripciones.map(i => (
                    <tr key={i.id}>
                      <td><span className="badge badge-gray">#{i.id}</span></td>
                      <td><span className="badge badge-blue">Alumno #{i.alumnoId}</span></td>
                      <td><span className="badge badge-blue">Curso #{i.cursoId}</span></td>
                      <td>{new Date(i.fechaInscripcion).toLocaleDateString('es-AR')}</td>
                      <td>
                        <span className={`badge ${i.estado === 'activa' ? 'badge-green' : 'badge-red'}`}>
                          {i.estado}
                        </span>
                      </td>
                      <td>
                        <div className="actions">
                          {i.estado === 'activa' && (
                            <button className="btn btn-warning" onClick={() => handleBaja(i.id)}>
                              ↩ Baja
                            </button>
                          )}
                          <button className="btn btn-danger" onClick={() => eliminar(i.id)}>
                            🗑
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>

        <div className="card">
          <p className="card-title">+ Nueva Inscripción</p>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>ID del Alumno</label>
              <input type="number" min="1" placeholder="Ej: 1" value={form.alumnoId}
                onChange={e => setForm({ ...form, alumnoId: e.target.value })} required />
            </div>
            <div className="form-group">
              <label>ID del Curso</label>
              <input type="number" min="1" placeholder="Ej: 2" value={form.cursoId}
                onChange={e => setForm({ ...form, cursoId: e.target.value })} required />
            </div>
            <div className="form-group">
              <label>Cupo máximo del curso</label>
              <input type="number" min="1" value={form.cupoMaximoCurso}
                onChange={e => setForm({ ...form, cupoMaximoCurso: e.target.value })} required />
            </div>
            <button type="submit" className="btn btn-primary">Inscribir Alumno</button>
          </form>
          <div style={{ marginTop: '1rem', padding: '0.75rem', background: '#f8fafc', borderRadius: '8px', fontSize: '0.8rem', color: '#64748b' }}>
            <strong>Reglas:</strong><br />
            · Máx. 5 inscripciones activas por alumno<br />
            · No se puede inscribir dos veces al mismo curso<br />
            · El curso no puede superar su cupo máximo
          </div>
        </div>
      </div>
    </div>
  );
}

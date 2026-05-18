import { useState, useEffect, useCallback } from 'react';
import * as alumnoService from '../services/alumnoService';

export const useAlumnos = () => {
  const [alumnos, setAlumnos]   = useState([]);
  const [loading, setLoading]   = useState(false);
  const [error, setError]       = useState(null);

  const fetchAlumnos = useCallback(async () => {
    setLoading(true);
    try {
      const data = await alumnoService.getAlumnos();
      setAlumnos(Array.isArray(data) ? data : []);
    } catch {
      setError('No se pudo conectar con alumno-service (puerto 3001)');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { fetchAlumnos(); }, [fetchAlumnos]);

  const crear = async (datos) => {
    const resultado = await alumnoService.createAlumno(datos);
    if (!resultado.error) setAlumnos(prev => [...prev, resultado]);
    return resultado;
  };

  const eliminar = async (id) => {
    await alumnoService.deleteAlumno(id);
    setAlumnos(prev => prev.filter(a => a.id !== id));
  };

  return { alumnos, loading, error, crear, eliminar, refetch: fetchAlumnos };
};

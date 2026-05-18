import { useState, useEffect, useCallback } from 'react';
import * as cursoService from '../services/cursoService';

export const useCursos = () => {
  const [cursos, setCursos]   = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError]     = useState(null);

  const fetchCursos = useCallback(async () => {
    setLoading(true);
    try {
      const data = await cursoService.getCursos();
      setCursos(Array.isArray(data) ? data : []);
    } catch {
      setError('No se pudo conectar con curso-service (puerto 3002)');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { fetchCursos(); }, [fetchCursos]);

  const crear = async (datos) => {
    const resultado = await cursoService.createCurso(datos);
    if (!resultado.error) setCursos(prev => [...prev, resultado]);
    return resultado;
  };

  const eliminar = async (id) => {
    await cursoService.deleteCurso(id);
    setCursos(prev => prev.filter(c => c.id !== id));
  };

  return { cursos, loading, error, crear, eliminar, refetch: fetchCursos };
};

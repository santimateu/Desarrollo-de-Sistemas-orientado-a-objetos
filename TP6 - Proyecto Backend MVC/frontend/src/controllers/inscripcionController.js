import { useState, useEffect, useCallback } from 'react';
import * as inscripcionService from '../services/inscripcionService';

export const useInscripciones = () => {
  const [inscripciones, setInscripciones] = useState([]);
  const [loading, setLoading]             = useState(false);
  const [error, setError]                 = useState(null);

  const fetchInscripciones = useCallback(async () => {
    setLoading(true);
    try {
      const data = await inscripcionService.getInscripciones();
      setInscripciones(Array.isArray(data) ? data : []);
    } catch {
      setError('No se pudo conectar con inscripcion-service (puerto 3003)');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { fetchInscripciones(); }, [fetchInscripciones]);

  const crear = async (datos) => {
    const resultado = await inscripcionService.createInscripcion(datos);
    if (!resultado.error) setInscripciones(prev => [...prev, resultado]);
    return resultado;
  };

  const darBaja = async (id) => {
    const resultado = await inscripcionService.darBajaInscripcion(id);
    if (!resultado.error) {
      setInscripciones(prev =>
        prev.map(i => i.id === id ? { ...i, estado: 'baja' } : i)
      );
    }
    return resultado;
  };

  const eliminar = async (id) => {
    await inscripcionService.deleteInscripcion(id);
    setInscripciones(prev => prev.filter(i => i.id !== id));
  };

  return { inscripciones, loading, error, crear, darBaja, eliminar, refetch: fetchInscripciones };
};

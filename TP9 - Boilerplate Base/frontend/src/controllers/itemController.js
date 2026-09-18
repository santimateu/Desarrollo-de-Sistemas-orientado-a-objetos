import { useState, useEffect, useCallback } from 'react';
import * as itemService from '../services/itemService';

export const useItems = () => {
  const [items, setItems]     = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError]     = useState(null);

  const fetchItems = useCallback(async () => {
    setLoading(true);
    try {
      const data = await itemService.getItems();
      setItems(Array.isArray(data) ? data : []);
      setError(null);
    } catch {
      setError('No se pudo conectar con el backend (puerto 3001)');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { fetchItems(); }, [fetchItems]);

  const crear = async (datos) => {
    const resultado = await itemService.createItem(datos);
    if (!resultado.error) setItems(prev => [...prev, resultado]);
    return resultado;
  };

  const eliminar = async (id) => {
    await itemService.deleteItem(id);
    setItems(prev => prev.filter(i => i.id !== id));
  };

  return { items, loading, error, crear, eliminar, refetch: fetchItems };
};

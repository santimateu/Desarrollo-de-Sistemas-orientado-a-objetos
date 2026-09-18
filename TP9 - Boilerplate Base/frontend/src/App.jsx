import { useState } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import ItemsView from './components/ItemsView';
import './index.css';

// Para sumar una entidad: agregar una entrada acá y su vista abajo
const tabs = [
  { id: 'items', label: '📦 Items' },
];

export default function App() {
  const [activeTab, setActiveTab] = useState('items');

  return (
    <div className="app">
      <Header activeTab={activeTab} tabs={tabs} onTabChange={setActiveTab} />
      <main className="main">
        {activeTab === 'items' && <ItemsView />}
      </main>
      <Footer />
    </div>
  );
}

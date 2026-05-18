import { useState } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import AlumnosView from './components/AlumnosView';
import CursosView from './components/CursosView';
import InscripcionesView from './components/InscripcionesView';
import './index.css';

const tabs = [
  { id: 'alumnos',       label: '👨‍🎓 Alumnos' },
  { id: 'cursos',        label: '📚 Cursos' },
  { id: 'inscripciones', label: '📋 Inscripciones' },
];

export default function App() {
  const [activeTab, setActiveTab] = useState('alumnos');

  return (
    <div className="app">
      <Header activeTab={activeTab} tabs={tabs} onTabChange={setActiveTab} />
      <main className="main">
        {activeTab === 'alumnos'       && <AlumnosView />}
        {activeTab === 'cursos'        && <CursosView />}
        {activeTab === 'inscripciones' && <InscripcionesView />}
      </main>
      <Footer />
    </div>
  );
}

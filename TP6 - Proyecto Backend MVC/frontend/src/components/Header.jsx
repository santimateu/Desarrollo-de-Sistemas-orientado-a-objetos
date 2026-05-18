export default function Header({ activeTab, tabs, onTabChange }) {
  return (
    <header className="header">
      <div className="header-top">
        <span className="header-icon">🎓</span>
        <div>
          <h1>Gestión de Alumnos y Cursos</h1>
          <p className="header-sub">Microservicios · Node.js + React · MVC</p>
        </div>
      </div>
      <nav className="tabs">
        {tabs.map(tab => (
          <button
            key={tab.id}
            className={`tab-btn ${activeTab === tab.id ? 'active' : ''}`}
            onClick={() => onTabChange(tab.id)}
          >
            {tab.label}
          </button>
        ))}
      </nav>
    </header>
  );
}

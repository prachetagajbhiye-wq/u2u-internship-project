function Navbar() {
  return (
    <nav className="navbar">

      <div className="logo">
        <span className="logo-icon">🎓</span>
        <div>
          <h2>AI Learning</h2>
          <p>Powered by Gemini</p>
        </div>
      </div>

      <ul className="nav-links">
        <li>Home</li>
        <li>Features</li>
        <li>Docs</li>
        <li>About</li>
      </ul>

      <button className="theme-btn">
        🌙
      </button>

    </nav>
  );
}

export default Navbar;
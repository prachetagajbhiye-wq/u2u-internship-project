function Hero() {
  return (
    <section className="hero">

      <div className="hero-pill">
        🚀 AI Powered Learning Platform
      </div>

      <h1>
        Your Personal
        <br />
        AI Study Assistant
      </h1>

      <p>
        Search your knowledge base instantly or let Gemini AI answer
        educational questions using Retrieval Augmented Generation (RAG).
      </p>

      <div className="hero-buttons">

        <button className="primary-btn">
          Start Learning
        </button>

        <button className="secondary-btn">
          Explore Features
        </button>

      </div>

      <div className="stats">

        <div className="stat-card">
          <h2>1072</h2>
          <p>📚 Documents</p>
        </div>

        <div className="stat-card">
          <h2>2692</h2>
          <p>🧠 Embeddings</p>
        </div>

        <div className="stat-card">
          <h2>4</h2>
          <p>📄 Sources</p>
        </div>

        <div className="stat-card">
          <h2>Gemini</h2>
          <p>🤖 AI Model</p>
        </div>

      </div>

    </section>
  );
}

export default Hero;
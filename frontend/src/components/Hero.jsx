import { useState } from "react";

function Hero() {
  const [inputQuestion, setInputQuestion] = useState("");
  const [result, setResult] = useState(null);

  const askQuestion = async () => {
    if (!inputQuestion.trim()) {
      alert("Please enter a question.");
      return;
    }

    const response = await fetch(
      `http://127.0.0.1:5000/answer?question=${encodeURIComponent(inputQuestion)}`
    );

    const data = await response.json();
    setResult(data);
  };

  const getRandomQuestion = async () => {
    const response = await fetch("http://127.0.0.1:5000/random-question");
    const data = await response.json();

    setResult(data);
  };

  return (
    <section className="hero">
      <h1>AI-Powered Educational Learning Platform</h1>

      <p>
        Learn smarter with AI-generated answers,
        educational resources,
        and personalized learning.
      </p>

      <input
        type="text"
        placeholder="Ask a question..."
        value={inputQuestion}
        onChange={(e) => setInputQuestion(e.target.value)}
      />

      <br />
      <br />

      <button onClick={askQuestion}>
        Ask
      </button>

      <button
        onClick={getRandomQuestion}
        style={{ marginLeft: "10px" }}
      >
        Random Question
      </button>

     {result && (
  <div className="question-card">
    {result.message ? (
      <p><strong>{result.message}</strong></p>
    ) : (
      <>
        <h2>{result.question}</h2>

        <p>
          <strong>Answer:</strong> {result.answer}
        </p>

        <p>
          <strong>Subject:</strong> {result.subject}
        </p>

        <p>
          <strong>Difficulty:</strong> {result.difficulty}
        </p>
      </>
    )}

  </div>
)}
    </section>
  );
}

export default Hero;
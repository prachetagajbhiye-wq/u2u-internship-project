import { useState, useEffect, useRef } from "react";

function ChatBox() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  const askQuestion = async () => {
    if (!question.trim()) return;

    const currentQuestion = question;

    setQuestion("");
    setLoading(true);

    try {
      const res = await fetch(
        `http://127.0.0.1:5000/answer?question=${encodeURIComponent(currentQuestion)}`
      );

      const data = await res.json();

      setMessages((prev) => [
        ...prev,
        {
          question: currentQuestion,
          ...data,
        },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          question: currentQuestion,
          answer: "Something went wrong. Please try again.",
          source: "Error",
          subject: "",
          difficulty: "",
        },
      ]);
    }

    setLoading(false);
  };

  const copyAnswer = async (text) => {
    await navigator.clipboard.writeText(text);
    alert("Answer copied!");
  };

  return (
    <div className="chat-box">

      <h2>💬 AI Assistant</h2>

      <div className="input-area">

        <input
          type="text"
          placeholder="Ask anything..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              askQuestion();
            }
          }}
        />

        <button onClick={askQuestion}>
          🚀 Ask AI
        </button>

      </div>

      <div className="chat-history">

        {messages.map((message, index) => (

          <div key={index} className="conversation">

            <div className="user-message">

              <strong>👤 You</strong>

              <p>{message.question}</p>

            </div>

            <div className="answer-card">

              <div className="answer-header">

                <span className="badge">
                  {message.source}
                </span>

                <button
                  className="copy-btn"
                  onClick={() => copyAnswer(message.answer)}
                >
                  📋 Copy
                </button>

              </div>

              <strong>🤖 AI Assistant</strong>

              <p style={{ whiteSpace: "pre-wrap" }}>
                {message.answer}
              </p>

              <div className="meta">

                <span>📚 {message.subject}</span>

                <span>⭐ {message.difficulty}</span>

              </div>

            </div>

          </div>

        ))}

        {loading && (

          <div className="thinking-card">

            🤖 AI is thinking...

          </div>

        )}

        <div ref={bottomRef}></div>

      </div>

    </div>
  );
}

export default ChatBox;
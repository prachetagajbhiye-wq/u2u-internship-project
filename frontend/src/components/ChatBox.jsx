import { useState, useEffect, useRef } from "react";

function ChatBox() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const fileInputRef = useRef(null);
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
        `http://127.0.0.1:5000/answer?question=${encodeURIComponent(
          currentQuestion
        )}`
      );

      const data = await res.json();

      setMessages((prev) => [
        ...prev,
        {
          question: currentQuestion,
          time: new Date().toLocaleTimeString(),
          ...data,
        },
      ]);

    } catch {
      setMessages((prev) => [
        ...prev,
        {
          question: currentQuestion,
          answer: "Something went wrong. Please try again.",
          source: [],
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

  const clearChat = () => {
    setMessages([]);
  };

  const uploadFile = async (event) => {
    const file = event.target.files[0];

    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      alert(data.message || "File uploaded successfully!");
    } catch {
      alert("Upload failed.");
    }
  };

  return (
    <div className="chat-box">

      <h2>💬 AI Learning Assistant</h2>

      <div className="suggestions">
        <p>💡 Try asking:</p>
        <div className="chips">
          <button onClick={() => setQuestion("What is an Operating System?")}>
            Operating System
          </button>
          <button onClick={() => setQuestion("Explain Process Scheduling")}>
            Process Scheduling
          </button>
          <button onClick={() => setQuestion("What is Deadlock?")}>
            Deadlock
          </button>

          <button onClick={() => setQuestion("Explain Threads")}>
            Threads
          </button>
        </div>
      </div>

      <div style={{ marginTop: "10px", marginBottom: "20px" }}>

        <button onClick={() => fileInputRef.current.click()}>
          📂 Upload File
        </button>

        <input
          ref={fileInputRef}
          type="file"
          style={{ display: "none" }}
          onChange={uploadFile}
        />

        <button
          style={{ marginLeft: "10px" }}
          onClick={clearChat}
        >
          🗑 Clear Chat
        </button>

      </div>

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
                  📚 Knowledge Base
                </span>

                <button
                  className="copy-btn"
                  onClick={() => copyAnswer(message.answer)}
                >
                  📋 Copy
                </button>

              </div>

              <strong>🤖 AI Assistant</strong>
              <div className="time">
                {message.time}
              </div>
              <p style={{ whiteSpace: "pre-wrap" }}>
                {message.answer}
              </p>

              <div className="meta">

                <span>📚 {message.subject}</span>

                <span>⭐ {message.difficulty}</span>

              </div>

              {message.source && (

                <div className="sources">

                  <strong>📄 Sources</strong>

                  <ul>

                    {(Array.isArray(message.source)
                      ? message.source
                      : [message.source]
                    ).map((src, i) => (

                      <li key={i}>{src}</li>

                    ))}

                  </ul>

                </div>

              )}

            </div>

          </div>

        ))}

        {loading && (
          <div className="thinking-card">
            <div className="spinner"></div>
            <span>AI is thinking...</span>
          </div>
        )}

        <div ref={bottomRef}></div>

      </div>

    </div>
  );
}

export default ChatBox;
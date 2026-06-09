import { useState } from "react";


function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    setLoading(true);

    try {
      const result = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: message,
        }),
      });

      const data = await result.json();

      setResponse(data.response);

    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Local AI Agent</h1>

      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask something..."
      />

      <button onClick={sendMessage}>
        Send
      </button>

      <hr />

      <h3>Response:</h3>

      {loading ? (
        <p>Thinking...</p>
      ) : (
      <p>{response}</p>
    )}
    </div>
  );
}

export default App;

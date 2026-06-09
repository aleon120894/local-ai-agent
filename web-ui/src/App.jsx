import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
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

      <p>{response}</p>
    </div>
  );
}

export default App;

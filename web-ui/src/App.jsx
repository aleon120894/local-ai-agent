import { useState } from "react";
import "./App.css";


function App() {

  const [message, setMessage] = useState("");
  const [files, setFiles] = useState([]);
  
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (event) => {

    const file = event.target.files[0];

    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

  setFiles((prev) => [...prev, file.name]);
};

  const sendMessage = async () => {

    if (!message.trim()) {
      return;
    }

    setMessages((prev) => [ 
      ...prev, 
      { role: "user", 
        content: message,
       },
     ]);
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

      setMessages((prev) => [ 
        ...prev, 
        { 
          role: "assistant", 
          content: data.response,
         }, 
        ]);

      setMessage("");

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <h1>Local AI Agent</h1>
      <h3>Knowledge Base</h3>

      <ul className="files">
        {files.map((file, index) => (
        <li key={index}>
          📄 {file}
        </li>
  ))}
</ul>

      <div className="input-area">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask something..."
        />
        <button onClick={sendMessage}>
          Send
        </button>

        <label className="upload-button">
          📎 Upload
        <input
          type="file"
          hidden
          onChange={handleUpload}
        />
</label>
      </div>

      <hr />

      <div className="chat">
        {messages.map((msg, index) => (
        <div
          key={index}
          className={`message ${msg.role}`}
          >
        <strong>{msg.role}:</strong> {msg.content}
      </div>
      ))}

  {loading && <p>Thinking...</p>}
</div>

      {loading && <p>Thinking...</p>}
    </div>
  );
}

export default App;

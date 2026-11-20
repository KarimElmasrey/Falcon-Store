import React, { useState, useRef, useEffect } from 'react';
import './FalconChat.css'; // ملف الـ CSS الخاص بالتصميم

const API_URL = "http://127.0.0.1:5001/api/chat";

export default function FalconChat() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { sender: 'bot', text: "Welcome to Falcon Shop! 👋 Ask me about our collections, prices, sizes or offers." }
  ]);
  const [choices, setChoices] = useState(["Shop men", "Shop women", "Sneakers", "Accessories", "Offers"]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const sessionId = useRef("sess_" + Math.random().toString(36).substring(2, 9)).current;

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isOpen]);

  const sendMessage = async (textToSend) => {
    const text = textToSend || input;
    if (!text.trim() || loading) return;

    const userMessage = text.trim();
    setMessages(prev => [...prev, { sender: 'user', text: userMessage }]);
    if (!textToSend) setInput("");
    setLoading(true);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage, session_id: sessionId })
      });

      if (!response.ok) throw new Error("Network response was not ok");
      const data = await response.json();

      setMessages(prev => [...prev, { sender: 'bot', text: data.reply }]);
      if (data.choices && data.choices.length > 0) {
        setChoices(data.choices);
      }
    } catch (error) {
      setMessages(prev => [...prev, { sender: 'bot', text: "Couldn't connect to Falcon Shop right now. Please make sure the server is running." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="falcon-chat-root">
      {/* نافذة الشات */}
      {isOpen && (
        <div className="falcon-window is-open">
          <header className="falcon-header">
            <div className="falcon-brand">
              <div className="falcon-logo">✦</div>
              <div>
                <p className="falcon-title">
                  <span style={{ color: '#06c9e8' }}>Falcon</span> <span style={{ color: '#ec4899' }}>Shop</span>
                </p>
                <div className="falcon-subtitle">
                  <span className="falcon-online"></span>Shopping assistant
                </div>
              </div>
            </div>
            <button className="falcon-close" onClick={() => setIsOpen(false)}>×</button>
          </header>

          <div className="falcon-messages">
            {messages.map((msg, idx) => (
              <div key={idx} className={`falcon-message-row ${msg.sender}`}>
                <div className="falcon-bubble">{msg.text}</div>
              </div>
            ))}
            {loading && <div className="falcon-message-row bot"><div className="falcon-bubble">Falcon is typing...</div></div>}
            <div ref={messagesEndRef} />
          </div>

          <div className="falcon-chips">
            {choices.map((choice, idx) => (
              <button key={idx} className="falcon-chip" onClick={() => sendMessage(choice)}>
                {choice}
              </button>
            ))}
          </div>

          <form className="falcon-form" onSubmit={(e) => { e.preventDefault(); sendMessage(); }}>
            <input
              className="falcon-input"
              type="text"
              placeholder="Ask about products, offers or sizes..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              maxLength={1000}
            />
            <button className="falcon-send" type="submit" disabled={loading}>Send</button>
          </form>
        </div>
      )}

      {/* زر فتح وغلق الشات */}
      <button className="falcon-launcher" onClick={() => setIsOpen(!isOpen)}>
        ✦
      </button>
    </div>
  );
}
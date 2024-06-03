import React, { useState } from 'react';
import Message from '../Message/Message';
import './ChatInterface.css';

const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<string[]>(["오늘 당신에게 어떻게 도움을 줄까요?"]);
  const [input, setInput] = useState('');

  const sendMessage = () => {
    if (!input.trim()) return; // 빈 메시지는 전송하지 않음
    setMessages([...messages, input]);
    setInput(''); // 입력 필드 초기화
  };

  return (
    <main id="chat-interface">
      <header id="chat-header">
        <h1>Chat</h1>
      </header>
      <div id="chat-history">
        {messages.map((message, index) => (
          <Message key={index} text={message} />
        ))}
      </div>
      <footer id="chat-footer">
        <input
          type="text"
          id="chat-input"
          placeholder="Message Chat..."
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyPress={e => e.key === 'Enter' && sendMessage()}
        />
        <button id="send-button" onClick={sendMessage}>Send</button>
      </footer>
    </main>
  );
};

export default ChatInterface;

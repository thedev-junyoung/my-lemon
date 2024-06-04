import React from 'react';
import useChat from '../../hooks/useChat';
import Message from '../Message/Message';
import ChatInput from '../ChatInput/ChatInput';
import './ChatContent.css';

const ChatContent: React.FC = () => {
  const { messages, input, setInput, sendMessage } = useChat();

  return (
    <div className="content">
      <div id="chat-header">
        <h1>** 접속한 유저의 Role 에 따른 헤더표시**</h1>
      </div>
      <div id="chat-history">
        {messages.map((message, index) => (
          <Message key={index} text={message} />
        ))}
      </div>
      <ChatInput input={input} setInput={setInput} sendMessage={sendMessage} />
    </div>
  );
};

export default ChatContent;
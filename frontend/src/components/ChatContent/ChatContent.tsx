import React from 'react';
import useChat from '../../hooks/useChat';
import Message from '../Message/Message';
import ChatInput from '../ChatInput/ChatInput';
import Header from '../Header/Header';

const ChatContent: React.FC = () => {
  const { messages, input, setInput, sendMessage } = useChat();

  return (
    <div className="flex flex-col flex-1 bg-black text-white">
      <Header/>
      <div className="flex-1 p-4 overflow-y-auto">
        {messages.map((message, index) => (
          <Message key={index} text={message} />
        ))}
      </div>
      <ChatInput input={input} setInput={setInput} sendMessage={sendMessage} />
    </div>
  );
};

export default ChatContent;

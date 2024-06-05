import React, { useEffect } from 'react';
import useChat from '../../hooks/useChat';
import Message from '../Message/Message';
import ChatInput from '../ChatInput/ChatInput';
import Header from '../Header/Header';

// ChatContent 컴포넌트: 채팅 메시지와 입력 필드를 포함
const ChatContent: React.FC<{ content: string }> = ({ content }) => {
  const { messages, input, setInput, sendMessage, addExternalMessage } = useChat();

  // 외부에서 받아온 콘텐츠를 메시지에 추가
  useEffect(() => {
    if (content) {
      addExternalMessage(content);
    }
  }, [content, addExternalMessage]);

  return (
    <div className="flex flex-col flex-1 bg-[#101010] text-white">
      <Header />
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

// src/hooks/useChat.ts
import { useState, useCallback } from 'react';

// useChat 훅: 채팅 메시지와 입력 상태를 관리하는 커스텀 훅
const useChat = () => {
  const [messages, setMessages] = useState<string[]>(["법률상담이 필요하신가요? 현재의 상황과 궁금한 내용을 말씀해주세요. 도와드리겠습니다."]);
  const [input, setInput] = useState('');

  // sendMessage 함수: 입력된 메시지를 전송하고 메시지 리스트에 추가
  const sendMessage = () => {
    if (!input.trim()) return;
    setMessages([...messages, input]);
    setInput('');
  };

  // addExternalMessage 함수: 외부에서 받은 메시지를 메시지 리스트에 추가
  const addExternalMessage = useCallback((message: string) => {
    setMessages(prevMessages => [...prevMessages, message]);
  }, []);

  return {
    messages,
    input,
    setInput,
    sendMessage,
    addExternalMessage,
  };
};

export default useChat;

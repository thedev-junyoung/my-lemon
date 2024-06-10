// src/components/ChatInput/ChatInput.tsx
import React, { useRef, useEffect } from 'react';
import { ChatInputProps } from '../../types';
import SendBtn from '../Button/SendBtn';

// ChatInput 컴포넌트: 메시지 입력 필드와 전송 버튼을 포함
const ChatInput: React.FC<ChatInputProps> = ({ input, setInput, sendMessage }) => {
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const inputAreaRef = useRef<HTMLDivElement>(null);

  // useEffect 훅을 사용하여 input 상태가 변경될 때마다 텍스트 영역의 높이를 조절
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;

      if (inputAreaRef.current) {
        inputAreaRef.current.style.height = 'auto';
        inputAreaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
      }
    }
  }, [input]);

  // handleKeyDown 함수: Enter 키를 누르면 메시지를 전송하고, Shift+Enter는 줄바꿈
  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div id="chat-footer" className="flex flex-col items-center bg-[#202020] p-4">
      <div
        id="chat-footer-inputarea"
        ref={inputAreaRef}
        className="flex items-center bg-gray-200 rounded-full overflow-hidden px-2 mx-14"
        style={{ minHeight: '48px', maxHeight: '300px', borderRadius: '25px', width: '100%' }}
      >
        <textarea
          ref={textareaRef}
          id="chat-input"
          className="flex-1 pl-4 border-none resize-none text-black bg-gray-200 focus:outline-none text-xl overflow-auto"
          placeholder="Message To LEMON..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          style={{ lineHeight: '1.5', minHeight: '48px', maxHeight: '300', borderRadius: '25px' }}
        />
        <SendBtn onClick={sendMessage} />
      </div>
      <div className="text-white text-center mt-2">Legal monster는 실수할 수 있습니다. @LEMON</div>
    </div>
  );
};

export default ChatInput;

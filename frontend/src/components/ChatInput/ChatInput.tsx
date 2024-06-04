import React from 'react';
import './ChatInput.css';
import { ChatInputProps } from '../../types'
import Button from '../Button/Button';

const ChatInput: React.FC<ChatInputProps> = ({ input, setInput, sendMessage }) => {
  return (
    <footer id="chat-footer">
      <input
        type="text"
        id="chat-input"
        placeholder="Message To LEMON..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            sendMessage();
          }
        }}
      />
      <Button label={'Send'} onClick={function (): void {
        alert('버튼 이벤트 추가하기')
        // throw new Error('Function not implemented.');
      } }/>
    </footer>
  );
};

export default ChatInput;

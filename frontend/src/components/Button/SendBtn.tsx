import React from 'react';
import { ButtonProps } from '../../types';

// Button 컴포넌트: 버튼의 색깔을 동적으로 설정하기 위해 color 속성을 추가
const Button: React.FC<ButtonProps> = ({ onClick }) => {
  return (
    <div id="send-button-div" className="flex items-center justify-center">
      <button id="send-button" className="bg-white hover:bg-gray-300 text-black font-bold p-2 rounded-full h-full" onClick={onClick}>
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 32 32" className="icon-2xl">
          <path fillRule="evenodd" d="M15.192 8.906a1.143 1.143 0 0 1 1.616 0l5.143 5.143a1.143 1.143 0 0 1-1.616 1.616l-3.192-3.192v9.813a1.143 1.143 0 0 1-2.286 0v-9.813l-3.192 3.192a1.143 1.143 0 1 1-1.616-1.616z" clipRule="evenodd"></path>
        </svg>
      </button>
    </div>
  );
};

export default Button;

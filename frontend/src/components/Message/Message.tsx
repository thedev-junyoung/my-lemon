import React from 'react';
import { MessageProps } from '../../types';
// Message 컴포넌트: 개별 채팅 메시지를 렌더링
const Message: React.FC<MessageProps> = ({ text }) => {
  return (
    <div>
    <div>LEMON or 사용자</div>
    <div className="bg-[#252525] p-2 rounded mb-2 text-white">
      {text}
    </div>
    </div>
  );
};

export default Message;

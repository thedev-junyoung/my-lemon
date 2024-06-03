import React from 'react';

interface MessageProps {
  text: string;
}

const Message: React.FC<MessageProps> = ({ text }) => {
  return (
    <div className="message">{text}</div>
  );
};

export default Message;

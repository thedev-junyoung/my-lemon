import { useState } from 'react';

const useChat = () => {
    const [messages, setMessages] = useState<string[]>(["법률상담이 필요하신가요? 현재의 상황과 궁금한 내용을 말씀해주세요. 도와드리겠습니다."]);
    const [input, setInput] = useState('');

    const sendMessage = () => {
        if (!input.trim()) return;
        setMessages([...messages, input]);
        setInput('');
    };

    return {
        messages,
        input,
        setInput,
        sendMessage,
    };
};

export default useChat;
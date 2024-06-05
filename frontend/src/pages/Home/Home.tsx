import React, { useEffect } from 'react';
import Sidebar from '../../components/Sidebar/Sidebar';
import ChatContent from '../../components/ChatContent/ChatContent';
import useMenuHandler from '../../hooks/useMenuHandler';

// Home 컴포넌트: 사이드바와 채팅 컨텐츠를 포함하는 메인 페이지 컴포넌트
const Home: React.FC = () => {
  const { content, handleMenuItemClick } = useMenuHandler();


  return (
    <div id="home-page" className="flex h-screen">
      <Sidebar onMenuItemClick={handleMenuItemClick} />
      <ChatContent content={content} />
    </div>
  );
};

export default Home;

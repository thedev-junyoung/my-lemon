import React, { useState, useEffect } from 'react';
import Sidebar from '../../components/Sidebar/Sidebar';
import ChatContent from '../../components/ChatContent/ChatContent';
import useMenuHandler from '../../hooks/useMenuHandler';
// Home 컴포넌트: 사이드바와 채팅 컨텐츠를 포함하는 메인 페이지 컴포넌트
const Home: React.FC = () => {
  const [isSidebarOpen, setIsSidebarOpen] = useState<boolean>(false);
  const { content, handleMenuItemClick } = useMenuHandler();

  // 화면 크기 변화 감지 및 레이아웃 업데이트
  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth > 768 && isSidebarOpen) {
        setIsSidebarOpen(false); // 화면 크기 변화 시 사이드바 상태 초기화
      }
    };

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [isSidebarOpen]);

  // 화면 외부 클릭 시 사이드바 닫기
  const handleClickOutside = (event: MouseEvent) => {
    if (
      (event.target as HTMLElement).closest('#sidebar') ||
      (event.target as HTMLElement).closest('#hamburger-button')
    )
      return;
    setIsSidebarOpen(false);
  };

  useEffect(() => {
    if (isSidebarOpen) {
      document.addEventListener('click', handleClickOutside);
    } else {
      document.removeEventListener('click', handleClickOutside);
    }
    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  }, [isSidebarOpen]);

  return (
    <div id="home-page" className="flex h-screen">
      <Sidebar onMenuItemClick={handleMenuItemClick} isOpen={isSidebarOpen} setIsOpen={setIsSidebarOpen} />
      <div
        className={`flex-1 transition-all duration-300 flex flex-col h-screen ${
          isSidebarOpen ? 'md:ml-64' : ''
        }`}
        style={{ overflow: 'hidden' }}
      >
        <ChatContent content={content} isSidebarOpen={isSidebarOpen} setIsSidebarOpen={setIsSidebarOpen} />
      </div>
    </div>
  );
};

export default Home;

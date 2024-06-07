import React, { useState, useEffect } from 'react';
import MainSidebar from './MainSidebar';
import AdminSidebar from './AdminSidebar';
import NewSidebar from './NewSidebar';
import BottomMenu from './BottomMenu';
import { SidebarProps } from '../../types'
// Sidebar 컴포넌트: 사이드바를 렌더링하며, 각 타입에 따라 다른 사이드바를 표시


const Sidebar: React.FC<SidebarProps> = ({ onMenuItemClick, isOpen, setIsOpen }) => {
  const [sidebarType, setSidebarType] = useState('main');

// 사이드바 타입에 따라 사이드바 컴포넌트를 렌더링
const renderSidebar = () => {
    switch (sidebarType) {
      case 'main':
        return <MainSidebar onMenuItemClick={onMenuItemClick} />;
      case 'admin':
        return <AdminSidebar onMenuItemClick={onMenuItemClick} />;
      case 'new':
        return <NewSidebar onMenuItemClick={onMenuItemClick} />;
      default:
        return <MainSidebar onMenuItemClick={onMenuItemClick} />;
    }
  };

  // 사이드바 열림 상태에 따라 화면 크기 조정
  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth > 768 && isOpen) {
        setIsOpen(false);
      }
    };

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [isOpen, setIsOpen]);

  return (
    <>
      <aside
        id="sidebar"
        className={`fixed top-0 left-0 z-30 h-full w-64 bg-[#303030] text-white p-5 flex flex-col justify-between transition-transform transform ${
          isOpen ? 'translate-x-0' : '-translate-x-full'
        } md:relative md:translate-x-0 md:flex-shrink-0`}
      >
        <div className="input-group mb-4">
          <input
            className="form-control search-input text-white bg-[#333] border-none"
            type="text"
            placeholder="메뉴 검색"
            onKeyUp={(e) => console.log('Search:', e.currentTarget.value)}
          />
        </div>
        <div className="flex-grow overflow-y-auto">{renderSidebar()}</div>
        <hr className="my-3" />
        <BottomMenu />
        <div className="mt-3 flex space-x-2">
          <button onClick={() => setSidebarType('main')}>Main</button>
          <button onClick={() => setSidebarType('admin')}>Admin</button>
          <button onClick={() => setSidebarType('new')}>New</button>
        </div>
      </aside>

      {isOpen && (
        <div
          className="fixed inset-0 bg-black opacity-50 z-20 md:hidden"
          onClick={() => setIsOpen(false)}
        ></div>
      )}
    </>
  );
};

export default Sidebar;

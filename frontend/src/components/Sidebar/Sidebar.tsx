import React, { useState } from 'react';
import MainSidebar from './MainSidebar';
import AdminSidebar from './AdminSidebar';
import NewSidebar from './NewSidebar';
import BottomMenu from './BottomMenu';

// Sidebar 컴포넌트: 사이드바를 렌더링하며, 각 타입에 따라 다른 사이드바를 표시
const Sidebar: React.FC<{ onMenuItemClick: (title: string) => void }> = ({ onMenuItemClick }) => {
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

  return (
    <aside className="w-64 bg-[#303030] text-white p-5 flex flex-col justify-between">
      <div className="input-group mb-4">
        <input
          className="form-control search-input text-white bg-[#333] border-none"
          type="text"
          placeholder="메뉴 검색"
          onKeyUp={(e) => console.log('Search:', e.currentTarget.value)}
        />
      </div>
      <div className="flex-grow overflow-y-auto">
        {renderSidebar()}
      </div>
      <hr className="my-3" />
      <BottomMenu />
      <div className="mt-3 flex space-x-2">
        <button onClick={() => setSidebarType('main')}>Main</button>
        <button onClick={() => setSidebarType('admin')}>Admin</button>
        <button onClick={() => setSidebarType('new')}>New</button>
      </div>
    </aside>
  );
};

export default Sidebar;

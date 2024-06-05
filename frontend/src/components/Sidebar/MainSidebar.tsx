import React from 'react';
import { mainMenuData } from './SidebarData';
import MenuItem from './MenuItem';

// MainSidebar 컴포넌트: 메인 메뉴 데이터를 기반으로 메뉴 항목을 렌더링
const MainSidebar: React.FC<{ onMenuItemClick: (title: string) => void }> = ({ onMenuItemClick }) => {
  return (
    <div className="flex-grow overflow-y-auto">
      {mainMenuData.map((item, index) => (
        <MenuItem key={index} item={item} onMenuItemClick={onMenuItemClick} />
      ))}
    </div>
  );
};

export default MainSidebar;

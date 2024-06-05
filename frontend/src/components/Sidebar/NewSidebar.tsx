import React from 'react';
import { newMenuData } from './SidebarData'; // 새 사이드바 데이터가 필요하다면 여기에 정의
import MenuItem from './MenuItem';

// NewSidebar 컴포넌트: 새 메뉴 데이터를 기반으로 메뉴 항목을 렌더링
const NewSidebar: React.FC<{ onMenuItemClick: (title: string) => void }> = ({ onMenuItemClick }) => {
  return (
    <div className="flex-grow overflow-y-auto">
      {newMenuData.map((item, index) => (
        <MenuItem key={index} item={item} onMenuItemClick={onMenuItemClick} />
      ))}
    </div>
  );
};

export default NewSidebar;

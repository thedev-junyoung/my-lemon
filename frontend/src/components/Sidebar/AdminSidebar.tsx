import React from 'react';
import { adminMenuData } from './SidebarData';
import MenuItem from './MenuItem';

// AdminSidebar 컴포넌트: 관리자 메뉴 데이터를 기반으로 메뉴 항목을 렌더링
const AdminSidebar: React.FC<{ onMenuItemClick: (title: string) => void }> = ({ onMenuItemClick }) => {
  return (
    <div className="flex-grow overflow-y-auto">
      {adminMenuData.map((item, index) => (
        <MenuItem key={index} item={item} onMenuItemClick={onMenuItemClick} />
      ))}
    </div>
  );
};

export default AdminSidebar;

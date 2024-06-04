import React, { useState } from 'react';
import './Sidebar.css';
import { sidebarData } from './SidebarData';

interface MenuItemProps {
  item: {
    title: string;
    subMenu?: MenuItemProps['item'][];
  };
}

const MenuItem: React.FC<MenuItemProps> = ({ item }) => {
  const [open, setOpen] = useState(false);

  return (
    <div className="menu-item">
      <div className="menu-title" onClick={() => setOpen(!open)}>
        {item.title}
      </div>
      {open && item.subMenu && (
        <div className="sub-menu">
          {item.subMenu.map((subItem, index) => (
            <MenuItem key={index} item={subItem} />
          ))}
        </div>
      )}
    </div>
  );
};

const Sidebar: React.FC = () => {
  return (
    <aside id="sidebar">
      <div className="logo">
        <img src="/logo.png" alt="LEMON Logo" />
      </div>
      <div className="menu">
        {sidebarData.map((item, index) => (
          <MenuItem key={index} item={item} />
        ))}
      </div>
      <div className="bottom-menu">
        <button>관리메뉴</button>
        <button>로그인 관련</button>
        <button>시스템 오류 제보</button>
      </div>
    </aside>
  );
};

export default Sidebar;
import React, { useState } from 'react';
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
    <div className="mb-2">
      <div
        className="cursor-pointer py-2 font-bold hover:bg-[stone-600]"
        onClick={() => setOpen(!open)}
      >
        {item.title}
      </div>
      {open && item.subMenu && (
        <div className="pl-4">
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
    <aside className="w-64 bg-[#303030] text-white p-5 flex flex-col justify-between">
      <div className="logo mb-5">
        <img src="/logo.png" alt="LEMON Logo" className="w-full h-auto" />
      </div>
      <div className="flex-grow overflow-y-auto">
        {sidebarData.map((item, index) => (
          <MenuItem key={index} item={item} />
        ))}
      </div>
      <hr />
      <div className="mt-3 mx-3 ">
        <button className="w-full text-left py-2 hover:bg-stone-600">관리메뉴</button>
        <button className="w-full text-left py-2 hover:bg-stone-600">로그인 관련</button>
        <button className="w-full text-left py-2 hover:bg-stone-600">시스템 오류 제보</button>
      </div>
    </aside>
  );
};

export default Sidebar;

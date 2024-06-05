import React, { useState } from 'react';

interface MenuItemProps {
  item: {
    title: string;
    subMenu?: MenuItemProps['item'][];
  };
  onMenuItemClick: (title: string) => void;
}

// MenuItem 컴포넌트: 개별 메뉴 항목을 렌더링
const MenuItem: React.FC<MenuItemProps> = ({ item, onMenuItemClick }) => {
  const [open, setOpen] = useState(false);
  // 클릭 핸들러 함수: 서브메뉴가 없을 때만 onMenuItemClick 호출
  const handleItemClick = () => {
    if (!item.subMenu) {
      onMenuItemClick(item.title);
    } else {
      setOpen(!open);
    }
  };

  return (
    <div className="mb-2">
      <div
        className="cursor-pointer py-2 font-bold hover:bg-gray-600"
        onClick={handleItemClick}
      >
        {item.title}
      </div>
      {open && item.subMenu && (
        <div className="pl-4">
          {item.subMenu.map((subItem, index) => (
            <MenuItem key={index} item={subItem} onMenuItemClick={onMenuItemClick} />
          ))}
        </div>
      )}
    </div>
  );
};

export default MenuItem;

import React, { useState } from 'react';
import { MenuItemProps } from '../../types';


// MenuItem 컴포넌트: 개별 메뉴 항목을 렌더링
const MenuItem: React.FC<MenuItemProps> = ({ item, onMenuItemClick }) => {
  const [open, setOpen] = useState(false);
  // 클릭 핸들러 함수: 서브메뉴가 없을 때만 onMenuItemClick 호출
  const handleItemClick = () => {
    if (!item.subMenu) {
      // 서브메뉴가 없는 경우 API가 정의되지 않은 것으로 간주하고 클릭한 메뉴 항목의 제목을 기본 내용으로 출력
      onMenuItemClick(item.title);
    } else {
      // 서브메뉴가 있는 경우 서브메뉴를 토글
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

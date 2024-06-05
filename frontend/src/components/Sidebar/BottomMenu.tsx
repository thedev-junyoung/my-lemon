import React from 'react';

// BottomMenu 컴포넌트: 하단 메뉴 항목을 렌더링
const BottomMenu: React.FC = () => {
  return (
    <div className="mt-3 mx-3">
      <button className="w-full text-left py-2 hover:bg-gray-600">관리메뉴</button>
      <button className="w-full text-left py-2 hover:bg-gray-600">로그인 관련</button>
      <button className="w-full text-left py-2 hover:bg-gray-600">시스템 오류 제보</button>
    </div>
  );
};

export default BottomMenu;

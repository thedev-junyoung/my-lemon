import React, { useEffect, useState } from 'react';
import useAuth from '../../hooks/useAuth';
import { HeaderProps } from '../../types';


// Header 컴포넌트: 사용자 정보를 표시하고 로그인/로그아웃 기능을 제공
const Header: React.FC<HeaderProps> = ({ isSidebarOpen, setIsSidebarOpen }) => {
  const { user, login, logout } = useAuth();
  const [logoSrc, setLogoSrc] = useState<string>('/logo/logo150x75.png');

  const updateLogoSrc = () => {
    if (window.innerWidth <= 768) {
      setLogoSrc('/logo/logo100x50.png');
    } else {
      setLogoSrc('/logo/logo150x75.png');
    }
  };

  useEffect(() => {
    updateLogoSrc();
    window.addEventListener('resize', updateLogoSrc);

    return () => {
      window.removeEventListener('resize', updateLogoSrc);
    };
  }, []);

  return (
    <div className="flex justify-between items-center bg-[#202020] text-white p-4">
      {/* 햄버거 버튼 */}
      <button
        id="hamburger-button"
        className="text-white md:hidden text-3xl p-1" // 텍스트 크기와 패딩 조정
        onClick={() => setIsSidebarOpen(!isSidebarOpen)}
      >
        &#9776;
      </button>

      {/* 로고 */}
      <div className={`logo ${isSidebarOpen ? 'mx-auto' : ''}`}>
        <img src={logoSrc} alt="LEMON Logo" className="h-auto" />
      </div>

      {/* 사용자 정보와 로그아웃 버튼 */}
      <div className="flex items-center space-x-4">
        {user ? (
          <>
            <span>{user.username}</span>
            <img
              src={user.profileImage || '/default-profile.png'}
              alt="Profile"
              className="w-10 h-10 rounded-full"
            />
            <button className="bg-red-600 p-2 rounded" onClick={logout}>
              Logout
            </button>
          </>
        ) : (
          <button
            onClick={() => login('Sample User', 'user@example.com')}
            className="p-2 bg-blue-600 text-white rounded"
          >
            Login
          </button>
        )}
      </div>
    </div>
  );
};

export default Header;

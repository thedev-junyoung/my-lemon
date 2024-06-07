import React from 'react';
import useAuth from '../../hooks/useAuth';

// Header 컴포넌트: 사용자 정보를 표시하고 로그인/로그아웃 기능을 제공
const Header: React.FC = () => {
  const { user, login, logout } = useAuth();

  return (
    <div className="flex items-center justify-between bg-[#101010] p-4">
      <div className="logo">
        <img src="/logo/logo150x75.png" alt="LEMON Logo" className="h-12" />
      </div>
      <div className="flex items-center">
        {user ? (
          <>
            <span className="text-white mr-4">{user.username}</span>
            <img
              src={user.profileImage || '/default-profile.png'}
              alt="Profile"
              className="w-10 h-10 rounded-full"
            />
            <button onClick={logout} className="ml-4 p-2 bg-red-600 text-white rounded">Logout</button>
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

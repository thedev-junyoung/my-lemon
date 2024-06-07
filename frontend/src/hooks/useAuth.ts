import { useState } from 'react';
import { User } from '../types';

// useAuth 훅: 사용자 정보와 로그인 상태를 관리
const useAuth = () => {
  const [user, setUser] = useState<User | null>(null);

  // 로그인 함수
  const login = (username: string, email: string) => {
    // 가짜 사용자 데이터 설정
    const newUser: User = {
      id: Date.now(), // 실제로는 유니크한 ID가 필요함
      username: username,
      email: email,
      profileImage: '/path/to/profile.jpg' // 실제 프로필 이미지 경로
    };

    setUser(newUser);
  };

  // 로그아웃 함수
  const logout = () => {
    setUser(null);
  };

  return {
    user,
    login,
    logout,
  };
};

export default useAuth;

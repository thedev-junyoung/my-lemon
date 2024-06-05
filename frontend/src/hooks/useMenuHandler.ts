import { useState } from 'react';
import axiosInstance from '../api/axiosInstance';
// 메뉴 항목 클릭 핸들러 커스텀 훅
const useMenuHandler = () => {
  // 상태 변수: 외부에서 가져온 콘텐츠를 저장
  const [content, setContent] = useState<string>('');
  // 메뉴 항목 클릭 시 데이터 fetch
  const handleMenuItemClick = async (title: string) => {
    try {
      let response;
      console.log(`Fetching data for: ${title}`);
      switch (title) {
        case '고소장 - 상해':
          response = await axiosInstance.get('/api/injury');
          console.log('Response for /api/injury:', response.data);
          setContent(response.data.message);
          break;
        case '고소장 - 중상해':
          response = await axiosInstance.get('/api/severeInjury');
          console.log('Response for /api/severeInjury:', response.data);
          setContent(response.data.message);
          break;
        // 추가 케이스 설정...
        default:
          setContent('기본 내용');
      }
    } catch (error) {
      console.error('Error handling menu item click:', error);
      setContent('Error fetching data');
    }
  };

  return { content, handleMenuItemClick };
};

export default useMenuHandler;

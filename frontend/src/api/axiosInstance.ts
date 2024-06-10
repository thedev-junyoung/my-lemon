import axios from 'axios';

// Axios 인스턴스 생성
const axiosInstance = axios.create({
  //baseURL: 'http://localhost:3000', // 필요에 따라 기본 URL 설정
  //baseURL: 'http://127.0.0.1:8000', // 기본 URL 설정
  baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000', // 기본 URL 설정
  headers: {
    'Content-Type': 'application/json',
  },
});
// 요청 인터셉터 추가
// 전역 에러 핸들러 설정
axiosInstance.interceptors.response.use(
  response => response,
  error => {
    if (error.response) {
      console.log(error.response)
      switch (error.response.status) {
        case 400:
          alert(error.response.data.message || '잘못된 요청입니다.');
          break;
        case 401:
          alert(error.response.data.message || '인증이 필요합니다. 로그인 후 다시 시도하십시오.');
          break;
        case 403:
          alert(error.response.data.message || '접근이 금지되었습니다.');
          break;
        case 404:
          alert(error.response.data.message || '요청한 자원을 찾을 수 없습니다.');
          break;
        case 422:
          alert(error.response.data.message || '잘못된 요청입니다. 입력한 데이터를 확인하세요.');
          break;
        case 500:
          alert(error.response.data.message || '서버에 오류가 발생했습니다.');
          break;
        default:
          alert('알 수 없는 오류가 발생했습니다.');
          break;
      }
    } else {
      alert('네트워크 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.');
    }
    return Promise.reject(error);
  }
);
export default axiosInstance;

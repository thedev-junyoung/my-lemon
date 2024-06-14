import axios from 'axios';
import { handleApiError } from '../utils/errorHandler';

// Axios 인스턴스 생성
const axiosInstance = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

// 요청 인터셉터 추가
axiosInstance.interceptors.request.use(
  config => {
    // CSRF 토큰을 localStorage에서 가져와서 헤더에 추가
    const csrfToken = localStorage.getItem('csrf_token');
    if (csrfToken) {
      config.headers['X-CSRF-Token'] = csrfToken;
    }
    return config;
  },
  error => Promise.reject(error)
);


// 응답 인터셉터 추가
axiosInstance.interceptors.response.use(
  response => response,
  error => {
    if (error.response) {
      const errorMessage = handleApiError(error);
      console.error('axiosInstance error:', errorMessage);
      return Promise.reject(new Error(errorMessage)); // 공통 에러 메시지 생성 후 예외로 던짐
    } else {
      const errorMessage = '네트워크 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.';
      console.error('axiosInstance error:', errorMessage);
      return Promise.reject(new Error(errorMessage));
    }
  }
);

export default axiosInstance;

import axios from 'axios';

// Axios 인스턴스 생성
const axiosInstance = axios.create({
  //baseURL: 'http://localhost:3000', // 필요에 따라 기본 URL 설정
  baseURL: 'http://127.0.0.1:8000', // 기본 URL 설정
});
export default axiosInstance;

import axios from 'axios';

// 고소장 - 상해 데이터 가져오기
export const fetchDataForInjury = async () => {
  try {
    const response = await axios.get('/api/injury');
    return response.data;
  } catch (error) {
    console.error('Error fetching data for injury:', error);
    throw error;
  }
};

// 고소장 - 중상해 데이터 가져오기
export const fetchDataForSevereInjury = async () => {
  try {
    const response = await axios.get('/api/severeInjury');
    return response.data;
  } catch (error) {
    console.error('Error fetching data for severe injury:', error);
    throw error;
  }
};

// 추가적인 API 요청 함수들...

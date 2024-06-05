import axiosInstance from './axiosInstance';
import MockAdapter from 'axios-mock-adapter';

const mock = new MockAdapter(axiosInstance, { delayResponse: 200 });

// 고소장 - 상해 Mock 데이터
mock.onGet('/').reply(200, 'Mock data for 고소장 - 상해');

// 고소장 - 중상해 Mock 데이터
mock.onGet('/api/severeInjury').reply(200, 'Mock data for 고소장 - 중상해');

// 추가적인 Mock 데이터 설정...

export default mock;

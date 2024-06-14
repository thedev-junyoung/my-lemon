import axiosInstance from "./axiosInstance";

export const login = async (email: string, password: string) => {
  try {
    const response = await axiosInstance.post("/auth/login", {
      email,
      password,
    });
    return response;
  } catch (error) {
    // 이미 인터셉터에서 처리된 에러 메시지를 던지므로, 추가로 처리할 필요 없음
    throw error;
  }
};

export const kakaoLogin = async (response: any) => {
  try {
    // 실제 카카오 로그인 API 호출 로직 추가
    return response; // 예시
  } catch (error) {
    // 이미 인터셉터에서 처리된 에러 메시지를 던지므로, 추가로 처리할 필요 없음
    throw error;
  }
};

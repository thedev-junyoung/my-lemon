// index.ts - 타입 정의 파일
// 인터페이스를 통해 객체의 구조를 정의하여 TypeScript가 타입을 체크할 수 있게 합니다.
// 이 인터페이스는 객체가 문자열 키에 대해 문자열 배열을 값으로 갖는 것을 명시합니다.
export interface Categories {
  [key: string]: string[];
}

export interface MessageProps {
  text: string;
}

export interface User {
  id: number;
  username: string;
  email: string;
  password?: string; // 생성 및 업데이트 시에만 사용
  profileImage?: string;    // 프로필 이미지, 선택 사항
}

export interface ChatInputProps {
  input: string;
  setInput: (input: string) => void;
  sendMessage: () => void;
}

export interface ButtonProps {
  label: string;
  onClick: () => void;
//  color?: string;  // 추가된 색깔 속성
}

export interface MenuItemProps {
  item: {
    title: string;
    subMenu?: MenuItemProps['item'][];
  };
  onMenuItemClick: (title: string) => void;
}

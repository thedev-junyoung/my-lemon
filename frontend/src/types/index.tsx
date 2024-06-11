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

// src/types.ts
export interface ButtonProps {
  onClick?: () => void;
  className?: string;
  children?: React.ReactNode;
  type?: 'button' | 'submit' | 'reset';
  disabled?: boolean;
}

export interface MenuItemProps {
  item: {
    title: string;
    subMenu?: MenuItemProps['item'][];
  };
  onMenuItemClick: (title: string) => void;
}


export interface ChatContentProps {
  content: string;
  isSidebarOpen: boolean;
  setIsSidebarOpen: (open: boolean) => void;
}

export interface SidebarProps {
  onMenuItemClick: (title: string) => void;
  isOpen: boolean;
  setIsOpen: (isOpen: boolean) => void;
}

export interface HeaderProps {
  isSidebarOpen: boolean;
  setIsSidebarOpen: (open: boolean) => void;
}

export interface LogoProps {
  isResponsive?: boolean;
  isCentered?: boolean;
}

export interface InputFieldProps {
  label: string;
  type: string;
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  onBlur?: () => void;  // onBlur를 선택적으로 사용
  errorMessage?: string;
  required?: boolean;
}
